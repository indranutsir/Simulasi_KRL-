from config import (
    DT,
    MAX_ACCELERATION,
    MAX_DECELERATION,
    MAX_SPEED,
    TRACK_DISTANCE,
)
from station import StationManager


class Simulation:

    def __init__(self, sound_manager=None):

        self.time = 0.0
        self.sound = sound_manager

        self.time_data = []
        self.speed_data = []
        self.position_data = []

        self.stations = StationManager(sound_manager)

    def update(self, train, controls):

        throttle_acc = (controls.throttle / 5) * MAX_ACCELERATION
        brake_acc = (controls.brake / 4) * MAX_DECELERATION

        if controls.direction == 0:
            throttle_acc = 0

        # Interlock pintu: selama pintu terbuka, throttle diabaikan
        # supaya kereta tidak bisa jalan sebelum pintu tertutup.
        if self.stations.doors_open:
            throttle_acc = 0

        acceleration = throttle_acc - brake_acc

        train.update(acceleration, controls.direction, DT)

        if train.speed > MAX_SPEED:
            train.speed = MAX_SPEED

        if train.position < 0:
            train.position = 0
            train.speed = 0

        if train.position > TRACK_DISTANCE:
            train.position = TRACK_DISTANCE
            train.speed = 0

        self.stations.update(train, DT)

        if self.sound:
            is_braking_hard = controls.brake >= 3 and train.speed > 2
            self.sound.update_brake(is_braking_hard)

        self.time += DT

        self.time_data.append(self.time)
        self.speed_data.append(train.speed * 3.6)
        self.position_data.append(train.position)

    @property
    def finished(self):
        return self.stations.finished
