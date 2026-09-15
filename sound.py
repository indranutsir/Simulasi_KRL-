import pygame

from config import (
    SND_HORN,
    SND_BRAKE,
    SND_DOOR_OPEN,
    SND_DOOR_CLOSE,
    SND_DING,
)


class SoundManager:
    """
    Membungkus semua efek suara game dalam satu tempat.

    Kalau perangkat tidak punya output audio (misalnya saat
    dijalankan di server/CI tanpa speaker), mixer akan gagal
    di-init. Supaya game tetap bisa jalan tanpa crash, semua
    error suara ditangkap dan diabaikan (silent fallback).
    """

    def __init__(self):
        self.enabled = True

        try:
            pygame.mixer.init()
            self.horn = pygame.mixer.Sound(SND_HORN)
            self.brake = pygame.mixer.Sound(SND_BRAKE)
            self.door_open = pygame.mixer.Sound(SND_DOOR_OPEN)
            self.door_close = pygame.mixer.Sound(SND_DOOR_CLOSE)
            self.ding = pygame.mixer.Sound(SND_DING)
        except pygame.error:
            self.enabled = False

        self._brake_playing = False

    # ------------------------------------------------------------
    def play_horn(self):
        if self.enabled:
            self.horn.play()

    def play_door_open(self):
        if self.enabled:
            self.door_open.play()

    def play_door_close(self):
        if self.enabled:
            self.door_close.play()

    def play_ding(self):
        if self.enabled:
            self.ding.play()

    # ------------------------------------------------------------
    def update_brake(self, is_braking_hard):
        """
        Suara decitan rem hanya mulai diputar sekali saat rem pertama
        kali diinjak dalam (bukan berulang setiap frame).
        """
        if not self.enabled:
            return

        if is_braking_hard and not self._brake_playing:
            self.brake.play()
            self._brake_playing = True
        elif not is_braking_hard:
            self._brake_playing = False
