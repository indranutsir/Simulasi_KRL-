from config import (
    ROLLING_RESISTANCE,
    AIR_DRAG_COEFF,
    JERK_LIMIT,
)


class Train:
    """
    Merepresentasikan kereta dan keadaan fisiknya.

    Fisika yang dipakai:
    - Akselerasi tidak langsung berubah drastis, tapi didekati
      bertahap ke akselerasi target (jerk-limited) supaya gerakan
      terasa halus, seperti kereta sungguhan.
    - Ada hambatan gelinding (rolling resistance) yang selalu
      melawan arah gerak, dan hambatan udara yang sebanding
      dengan kuadrat kecepatan.
    """

    def __init__(self):
        self.position = 0.0
        self.speed = 0.0

        # Akselerasi aktual saat ini (m/s^2), dipakai untuk jerk-limiting
        self.acceleration = 0.0

    def update(self, target_acceleration, direction, dt):

        # --- Jerk limiting: akselerasi bergerak bertahap menuju target ---
        max_delta = JERK_LIMIT * dt
        delta = target_acceleration - self.acceleration
        delta = max(-max_delta, min(max_delta, delta))
        self.acceleration += delta

        # --- Terapkan akselerasi ke kecepatan ---
        self.speed += self.acceleration * dt

        # --- Hambatan alami (hanya berlaku saat kereta bergerak) ---
        if self.speed > 0:
            drag = ROLLING_RESISTANCE + AIR_DRAG_COEFF * (self.speed ** 2)
            self.speed -= drag * dt

        if self.speed < 0:
            self.speed = 0
            self.acceleration = 0

        self.position += self.speed * direction * dt

    def is_stopped(self):
        return self.speed < 0.05
