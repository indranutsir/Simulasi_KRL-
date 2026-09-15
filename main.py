import pygame

from config import *
from train import Train
from controls import Controls
from simulation import Simulation
from ui import UI
from sound import SoundManager
from graph import show_graphs

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Iclik Simulator")

icon = pygame.image.load(ICON)
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

ui = UI()
sound = SoundManager()

# ==========================================
# State game: "menu", "playing", "finished"
# ==========================================

STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_FINISHED = "finished"

state = STATE_MENU

train = None
controls = None
sim = None


def new_game():
    """Membuat ulang objek permainan untuk memulai/mengulang sesi."""
    global train, controls, sim
    train = Train()
    controls = Controls()
    sim = Simulation(sound)


running = True

while running:

    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_click = True

        if event.type == pygame.KEYDOWN and state == STATE_PLAYING:

            if event.key == pygame.K_w:
                controls.throttle_up()

            if event.key == pygame.K_s:
                controls.throttle_down()

            if event.key == pygame.K_a:
                controls.brake_down()

            if event.key == pygame.K_d:
                controls.brake_up()

            if event.key == pygame.K_f:
                if train.speed < 0.1:
                    controls.set_forward()

            if event.key == pygame.K_r:
                if train.speed < 0.1:
                    controls.set_reverse()

            if event.key == pygame.K_n:
                if train.speed < 0.1:
                    controls.set_neutral()

            if event.key == pygame.K_h:
                sound.play_horn()

    # ==========================================
    # MENU
    # ==========================================

    if state == STATE_MENU:

        if ui.start_button.is_clicked(mouse_pos, mouse_click):
            new_game()
            state = STATE_PLAYING

        ui.draw_menu(screen, mouse_pos)

    # ==========================================
    # BERMAIN
    # ==========================================

    elif state == STATE_PLAYING:

        sim.update(train, controls)

        screen.fill(BLACK)
        ui.draw_game(screen, train, controls, sim, mouse_pos)

        if sim.finished:
            state = STATE_FINISHED

    # ==========================================
    # SELESAI
    # ==========================================

    elif state == STATE_FINISHED:

        if ui.replay_button.is_clicked(mouse_pos, mouse_click):
            new_game()
            state = STATE_PLAYING

        if ui.graph_button.is_clicked(mouse_pos, mouse_click):
            show_graphs(sim)

        ui.draw_finished(screen, sim, mouse_pos)

    pygame.display.update()

pygame.quit()
