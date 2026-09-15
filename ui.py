import pygame
from config import *


class Button:
    """Tombol sederhana berbentuk kotak dengan label teks."""

    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_click):
        return mouse_click and self.rect.collidepoint(mouse_pos)

    def draw(self, screen, font, mouse_pos, base_color, hover_color, text_color=WHITE):
        hovered = self.is_hovered(mouse_pos)
        color = hover_color if hovered else base_color

        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, WHITE, self.rect, width=2, border_radius=8)

        label = font.render(self.text, True, text_color)
        label_rect = label.get_rect(center=self.rect.center)
        screen.blit(label, label_rect)


class UI:

    def __init__(self):

        self.font = pygame.font.SysFont("arial", 24)
        self.small_font = pygame.font.SysFont("arial", 18)
        self.big_font = pygame.font.SysFont("arial", 32)
        self.title_font = pygame.font.SysFont("arial", 56, bold=True)

        self.background = pygame.image.load(BACKGROUND).convert()
        self.background = pygame.transform.scale(
            self.background,
            (1983, 527 - 150)
        )
        self.ground = pygame.image.load(TANAH).convert_alpha()
        self.ground = pygame.transform.scale(self.ground, (WINDOW_WIDTH, 100))
        self.track = pygame.image.load(REL).convert_alpha()
        self.track = pygame.transform.scale(self.track, (1000, 40))
        self.train = pygame.image.load(KRL).convert_alpha()
        w, h = self.train.get_size()
        new_width = 700
        new_height = int(h * new_width / w)
        self.train = pygame.transform.smoothscale(self.train, (new_width, new_height))

        self.station_images = [
            pygame.transform.scale(
                pygame.image.load(path).convert_alpha(),
                (WINDOW_WIDTH, 200)
            )
            for path in STASIUN
        ]

        # Tombol-tombol (posisi didefinisikan sekali, dipakai di layar terkait)
        self.start_button = Button((WINDOW_WIDTH // 2 - 110, 480, 220, 60), "MULAI")
        self.replay_button = Button((WINDOW_WIDTH // 2 - 240, 600, 220, 60), "MAIN LAGI")
        self.graph_button = Button((WINDOW_WIDTH // 2 + 20, 600, 220, 60), "LIHAT GRAFIK")

    # ==========================================
    # MENU AWAL
    # ==========================================

    def draw_menu(self, screen, mouse_pos):

        screen.fill(MENU_BG)

        title = self.title_font.render("ICLIK SIMULATOR", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        screen.blit(title, title_rect)

        subtitle = self.font.render(
            "Simulator Masinis KRL - Berhentikan kereta setepat mungkin di stasiun!",
            True, LIGHT_GRAY
        )
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 210))
        screen.blit(subtitle, subtitle_rect)

        controls_lines = [
            "W : Tambah Throttle        S : Kurangi Throttle",
            "D : Tambah Rem              A : Kurangi Rem",
            "F : Maju     N : Netral     R : Mundur",
            "H : Klakson",
        ]
        for i, line in enumerate(controls_lines):
            text = self.font.render(line, True, WHITE)
            rect = text.get_rect(center=(WINDOW_WIDTH // 2, 300 + i * 34))
            screen.blit(text, rect)

        self.start_button.draw(screen, self.big_font, mouse_pos, GREEN, (0, 240, 0))

    # ==========================================
    # LAYAR UTAMA (BERMAIN)
    # ==========================================

    def draw_game(self, screen, train, controls, sim, mouse_pos):
        self.draw_header(screen, train, sim)
        self.draw_body(screen, train, sim)
        self.draw_footer(screen, controls)
        self.draw_notification(screen, sim)

    def draw_header(self, screen, train, sim):

        pygame.draw.rect(screen, HEADER_COLOR, (0, 0, WINDOW_WIDTH, HEADER_HEIGHT))

        speed_text = self.big_font.render(f"Speed : {train.speed * 3.6:.1f} km/h", True, WHITE)
        pos_text = self.font.render(f"Position : {train.position:.1f} m", True, WHITE)
        time_text = self.font.render(f"Time : {sim.time:.1f} s", True, WHITE)

        station_name = sim.stations.current_station_name(train)
        station_text = self.font.render(f"Menuju : {station_name}", True, YELLOW)

        score_text = self.font.render(
            f"Skor : {sim.stations.total_score}/{sim.stations.max_score}",
            True, GOLD
        )

        screen.blit(speed_text, (20, 15))
        screen.blit(pos_text, (20, 60))
        screen.blit(time_text, (320, 60))
        screen.blit(station_text, (520, 15))
        screen.blit(score_text, (520, 60))

        # Indikator pintu
        door_color = GREEN if sim.stations.doors_open else GRAY
        door_label = "PINTU TERBUKA" if sim.stations.doors_open else "PINTU TERTUTUP"
        door_text = self.font.render(door_label, True, door_color)
        screen.blit(door_text, (920, 38))

    def draw_body(self, screen, train, sim):

        # Background
        screen.blit(self.background, (0, HEADER_HEIGHT))

        # Tanah Belakang
        ground_width = self.ground.get_width()
        ground_scroll = int(train.position * 0.2) % ground_width

        for ground_height, ground_y in [
            (125, HEADER_HEIGHT + BODY_HEIGHT - 125),
            (85, HEADER_HEIGHT + BODY_HEIGHT - 85),
        ]:
            for x in range(-ground_width - ground_scroll, WINDOW_WIDTH + ground_width, ground_width):
                screen.blit(self.ground, (x, ground_y))

        # Rel
        track_width = self.track.get_width()
        offset = int(train.position % track_width)

        for x in range(-track_width + offset, WINDOW_WIDTH + track_width, track_width):
            screen.blit(self.track, (x, 500))

        # Stasiun
        station_height = self.station_images[0].get_height()

        for i, station in enumerate(sim.stations.stations):
            station_img = self.station_images[i % len(self.station_images)]
            screen_x = station.position - train.position * 0.8
            station_w = station_img.get_width()

            if -station_w - 100 <= screen_x <= WINDOW_WIDTH + 100:
                screen.blit(station_img, (screen_x, 500 - station_img.get_height()))

                # Label nama stasiun di atas gambar stasiun
                label = self.small_font.render(station.name, True, WHITE)
                label_rect = label.get_rect(
                    center=(screen_x + station_w / 2, 500 - station_height - 15)
                )
                screen.blit(label, label_rect)

        # Kereta (kamera terkunci ke kereta)
        train_x = 250
        screen.blit(self.train, (train_x, 505 - self.train.get_height()))

        # Indikator pintu di sisi kereta
        if sim.stations.doors_open:
            door_rect = pygame.Rect(train_x + 60, 505 - self.train.get_height() + 20, 40, 40)
            pygame.draw.rect(screen, GREEN, door_rect, border_radius=6)

        # Tanah Depan
        ground_width = self.ground.get_width()
        ground_scroll = int(train.position * 0.4) % ground_width

        for x in range(-ground_width - ground_scroll, WINDOW_WIDTH + ground_width, ground_width):
            screen.blit(self.ground, (x, HEADER_HEIGHT + BODY_HEIGHT - 85))

    def draw_footer(self, screen, controls):

        y = WINDOW_HEIGHT - FOOTER_HEIGHT

        pygame.draw.rect(screen, FOOTER_COLOR, (0, y, WINDOW_WIDTH, FOOTER_HEIGHT))

        # Throttle
        throttle_text = self.font.render(f"Throttle : {controls.throttle}", True, WHITE)
        screen.blit(throttle_text, (50, y + 20))
        pygame.draw.rect(screen, GRAY, (250, y + 20, 300, 30))
        pygame.draw.rect(screen, GREEN, (250, y + 20, controls.throttle / 5 * 300, 30))

        # Rem
        brake_text = self.font.render(f"Brake : {controls.brake}", True, WHITE)
        screen.blit(brake_text, (50, y + 70))
        pygame.draw.rect(screen, GRAY, (250, y + 70, 300, 30))
        pygame.draw.rect(screen, RED, (250, y + 70, controls.brake / 4 * 300, 30))

        # Indikator arah
        title = self.font.render("Direction", True, WHITE)
        screen.blit(title, (700, y + 10))

        forward_color = GREEN if controls.direction == 1 else GRAY
        pygame.draw.circle(screen, forward_color, (760, y + 65), 20)
        screen.blit(self.font.render("F", True, WHITE), (753, y + 95))

        neutral_color = YELLOW if controls.direction == 0 else GRAY
        pygame.draw.circle(screen, neutral_color, (840, y + 65), 20)
        screen.blit(self.font.render("N", True, WHITE), (833, y + 95))

        reverse_color = RED if controls.direction == -1 else GRAY
        pygame.draw.circle(screen, reverse_color, (920, y + 65), 20)
        screen.blit(self.font.render("R", True, WHITE), (913, y + 95))

        help_text = self.font.render(
            "W/S : Throttle | A/D : Rem | F/N/R : Arah | H : Klakson",
            True, WHITE
        )
        screen.blit(help_text, (500, y + 115))

    def draw_notification(self, screen, sim):
        """Banner notifikasi hasil berhenti di stasiun, muncul sebentar lalu hilang."""

        if sim.stations.last_event_timer <= 0:
            return

        text = self.big_font.render(sim.stations.last_event_text, True, WHITE)
        banner_width = text.get_width() + 60
        banner_rect = pygame.Rect(0, 0, banner_width, 60)
        banner_rect.center = (WINDOW_WIDTH // 2, HEADER_HEIGHT + 50)

        panel = pygame.Surface((banner_rect.width, banner_rect.height), pygame.SRCALPHA)
        panel.fill((20, 20, 20, 190))
        screen.blit(panel, banner_rect.topleft)
        pygame.draw.rect(screen, GOLD, banner_rect, width=2, border_radius=8)

        text_rect = text.get_rect(center=banner_rect.center)
        screen.blit(text, text_rect)

    # ==========================================
    # LAYAR SELESAI / RINGKASAN
    # ==========================================

    def draw_finished(self, screen, sim, mouse_pos):

        screen.fill(MENU_BG)

        title = self.title_font.render("PERJALANAN SELESAI", True, WHITE)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 70))
        screen.blit(title, title_rect)

        panel_rect = pygame.Rect(WINDOW_WIDTH // 2 - 350, 130, 700, 40 * len(sim.stations.stations) + 30)
        pygame.draw.rect(screen, PANEL_COLOR, panel_rect, border_radius=10)

        header = self.font.render("Stasiun", True, LIGHT_GRAY)
        screen.blit(header, (panel_rect.x + 20, panel_rect.y + 10))
        header2 = self.font.render("Hasil", True, LIGHT_GRAY)
        screen.blit(header2, (panel_rect.x + 420, panel_rect.y + 10))
        header3 = self.font.render("Skor", True, LIGHT_GRAY)
        screen.blit(header3, (panel_rect.x + 580, panel_rect.y + 10))

        for i, station in enumerate(sim.stations.stations):
            row_y = panel_rect.y + 40 + i * 38
            label, score = station.label_and_score

            color = {
                "perfect": GOLD,
                "good": GREEN,
                "ok": BLUE,
                "skipped": RED,
            }.get(station.quality, WHITE)

            name_text = self.font.render(station.name, True, WHITE)
            result_text = self.font.render(label, True, color)
            score_text = self.font.render(str(score), True, color)

            screen.blit(name_text, (panel_rect.x + 20, row_y))
            screen.blit(result_text, (panel_rect.x + 420, row_y))
            screen.blit(score_text, (panel_rect.x + 580, row_y))

        total_text = self.big_font.render(
            f"Total Skor : {sim.stations.total_score} / {sim.stations.max_score}"
            f"  ({sim.stations.average_score:.0f}%)",
            True, GOLD
        )
        total_rect = total_text.get_rect(center=(WINDOW_WIDTH // 2, panel_rect.bottom + 50))
        screen.blit(total_text, total_rect)

        time_text = self.font.render(f"Total waktu tempuh : {sim.time:.1f} detik", True, WHITE)
        time_rect = time_text.get_rect(center=(WINDOW_WIDTH // 2, panel_rect.bottom + 90))
        screen.blit(time_text, time_rect)

        self.replay_button.draw(screen, self.font, mouse_pos, BLUE, (90, 180, 255))
        self.graph_button.draw(screen, self.font, mouse_pos, GRAY, LIGHT_GRAY)
