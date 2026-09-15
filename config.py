WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

HEADER_HEIGHT = 100
FOOTER_HEIGHT = 150

# ==========================================
# Assets (path memakai huruf besar "Assets"
# supaya konsisten dengan nama folder asli -
# ini juga yang bikin game gagal jalan di
# Linux/Mac sebelumnya karena path case-sensitive)
# ==========================================

ICON = "Assets/icon.png"
REL = "Assets/rel.png"
BACKGROUND = "Assets/background.png"
KRL = "Assets/KRL205.png"
TANAH = "Assets/tanah.png"

STASIUN = [
    "Assets/Stasiun/up.png",
    "Assets/Stasiun/ui.png",
    "Assets/Stasiun/poc.png",
    "Assets/Stasiun/dpb.png",
    "Assets/Stasiun/dp.png",
]

NAMA_STASIUN = [
    "Universitas Pancasila",
    "Universitas Indonesia",
    "Pondok Cina",
    "Depok Baru",
    "Depok",
]

POSISI_STASIUN = [0, 2460, 5400, 8130, 12670]

# Sound effects
SND_HORN = "Assets/Sounds/horn.wav"
SND_BRAKE = "Assets/Sounds/brake.wav"
SND_DOOR_OPEN = "Assets/Sounds/door_open.wav"
SND_DOOR_CLOSE = "Assets/Sounds/door_close.wav"
SND_DING = "Assets/Sounds/ding.wav"

BODY_Y = HEADER_HEIGHT
BODY_HEIGHT = WINDOW_HEIGHT - HEADER_HEIGHT - FOOTER_HEIGHT

FPS = 60
DT = 0.1

# ==========================================
# Fisika
# ==========================================

MAX_SPEED_KMH = 80
MAX_SPEED = MAX_SPEED_KMH / 3.6

MAX_ACCELERATION = 0.8   # m/s^2, dari throttle penuh
MAX_DECELERATION = 1.0   # m/s^2, dari rem penuh

# Hambatan alami (rolling resistance) - selalu melawan gerak,
# supaya kereta tidak melaju konstan selamanya walau throttle 0
ROLLING_RESISTANCE = 0.03    # m/s^2

# Hambatan udara, sebanding dengan kuadrat kecepatan
AIR_DRAG_COEFF = 0.0006      # m/s^2 per (m/s)^2

# Jerk limit: seberapa cepat akselerasi boleh berubah (m/s^3)
# supaya perpindahan throttle/rem terasa halus, bukan patah-patah
JERK_LIMIT = 2.5

TRACK_DISTANCE = 13000  # meter

# ==========================================
# Sistem Stasiun & Penilaian
# ==========================================

# Jarak toleransi berhenti (meter) dari titik target stasiun
STOP_TOLERANCE_PERFECT = 3      # "Perfect!"
STOP_TOLERANCE_GOOD = 10        # "Good"
STOP_TOLERANCE_OK = 25          # "OK"
# Di luar itu -> "Meleset"

# Jarak sebelum stasiun ketika kereta dianggap "memasuki" area
# pemberhentian (dipakai untuk deteksi lewat tanpa berhenti)
STATION_APPROACH_ZONE = 60

DOOR_OPEN_TIME = 3.0   # detik pintu terbuka otomatis saat berhenti pas

# ==========================================
# Warna
# ==========================================

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

GRAY = (70, 70, 70)
LIGHT_GRAY = (120, 120, 120)

GREEN = (0, 200, 0)
RED = (220, 50, 50)

BLUE = (50, 150, 255)
YELLOW = (230, 200, 40)
GOLD = (255, 200, 60)

HEADER_COLOR = (40, 40, 60)
FOOTER_COLOR = (40, 40, 60)
BODY_COLOR = (220, 220, 220)

MENU_BG = (25, 30, 45)
PANEL_COLOR = (35, 40, 60)
