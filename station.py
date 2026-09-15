from config import (
    NAMA_STASIUN,
    POSISI_STASIUN,
    STOP_TOLERANCE_PERFECT,
    STOP_TOLERANCE_GOOD,
    STOP_TOLERANCE_OK,
    STATION_APPROACH_ZONE,
    DOOR_OPEN_TIME,
)

# Status penyelesaian sebuah stasiun
PENDING = "pending"
STOPPED = "stopped"
SKIPPED = "skipped"

# Kualitas pemberhentian -> (label, skor)
QUALITY_TABLE = {
    "perfect": ("PERFECT!", 100),
    "good": ("Good", 75),
    "ok": ("OK", 50),
    "skipped": ("Terlewat", 0),
}


class Station:

    def __init__(self, index, name, position):
        self.index = index
        self.name = name
        self.position = position

        self.status = PENDING
        self.quality = None          # "perfect" / "good" / "ok" / "skipped"
        self.stop_error = None       # jarak (m) dari titik target saat berhenti
        self.entered_zone = False    # sudah pernah masuk approach zone?

    def resolve_stop(self, error):
        self.stop_error = error
        abs_err = abs(error)

        if abs_err <= STOP_TOLERANCE_PERFECT:
            self.quality = "perfect"
        elif abs_err <= STOP_TOLERANCE_GOOD:
            self.quality = "good"
        else:
            self.quality = "ok"

        self.status = STOPPED

    def resolve_skip(self):
        self.quality = "skipped"
        self.status = SKIPPED

    @property
    def label_and_score(self):
        if self.quality is None:
            return ("-", 0)
        return QUALITY_TABLE[self.quality]


class StationManager:
    """
    Mengelola daftar stasiun di sepanjang jalur: mendeteksi kapan
    kereta berhenti tepat/tidak tepat di sebuah stasiun, mengatur
    buka-tutup pintu otomatis, dan menghitung skor perjalanan.
    """

    def __init__(self, sound_manager=None):
        self.stations = [
            Station(i, name, pos)
            for i, (name, pos) in enumerate(zip(NAMA_STASIUN, POSISI_STASIUN))
        ]

        self.sound = sound_manager

        self.doors_open = False
        self.door_timer = 0.0
        self.active_station = None   # stasiun yang pintunya sedang terbuka

        self.last_event_text = ""    # untuk ditampilkan sebagai notifikasi UI
        self.last_event_timer = 0.0

        self.finished = False

    # ------------------------------------------------------------
    def _notify(self, text):
        self.last_event_text = text
        self.last_event_timer = 2.5

    # ------------------------------------------------------------
    def update(self, train, dt):

        # Timer notifikasi UI
        if self.last_event_timer > 0:
            self.last_event_timer -= dt

        # --- Kalau pintu sedang terbuka, hitung mundur lalu tutup ---
        if self.doors_open:
            self.door_timer -= dt
            if self.door_timer <= 0:
                self.doors_open = False
                self.active_station = None
                if self.sound:
                    self.sound.play_door_close()
            return  # selama pintu terbuka, tidak perlu cek stasiun lain

        for station in self.stations:

            if station.status != PENDING:
                continue

            distance = station.position - train.position
            abs_distance = abs(distance)

            if abs_distance <= STATION_APPROACH_ZONE:
                station.entered_zone = True

                if train.is_stopped() and abs_distance <= STOP_TOLERANCE_OK:
                    station.resolve_stop(distance)
                    self._open_doors(station)
                    label, score = station.label_and_score
                    self._notify(f"{station.name}: {label} (+{score})")

            elif station.entered_zone and abs_distance > STATION_APPROACH_ZONE:
                # Sempat masuk zona tapi sekarang sudah menjauh lagi
                # tanpa pernah berhenti dalam toleransi -> dianggap terlewat
                station.resolve_skip()
                self._notify(f"{station.name}: Terlewat (+0)")

        if all(s.status != PENDING for s in self.stations):
            self.finished = True

    # ------------------------------------------------------------
    def _open_doors(self, station):
        self.doors_open = True
        self.door_timer = DOOR_OPEN_TIME
        self.active_station = station
        if self.sound:
            if station.quality == "perfect":
                self.sound.play_ding()
            self.sound.play_door_open()

    # ------------------------------------------------------------
    def current_station_name(self, train):
        """Nama stasiun terdekat yang belum selesai, untuk ditampilkan di UI."""
        pending = [s for s in self.stations if s.status == PENDING]
        if not pending:
            return self.stations[-1].name if self.stations else ""
        nearest = min(pending, key=lambda s: abs(s.position - train.position))
        return nearest.name

    # ------------------------------------------------------------
    @property
    def total_score(self):
        return sum(s.label_and_score[1] for s in self.stations)

    @property
    def max_score(self):
        return len(self.stations) * 100

    @property
    def average_score(self):
        if not self.stations:
            return 0
        return self.total_score / len(self.stations)
