from enum import Enum

import pygame
import webcolors as color

import game
import menu
import audio
import curve
import util

class State(Enum):
    START = 0
    MAIN = 1
    SETUP = 2
    PLAY = 3
    PAUSE = 4
    END = 5
    EXIT = 6

# setup config
config = util.get_config("config.yml")

# main function
if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption("Curve")

    clock = pygame.time.Clock()

    # set window size
    display = pygame.display.set_mode((config["SCREEN"]["WIDTH"], config["SCREEN"]["HEIGHT"]))

    pygame.display.update()

    config_curves = []
    curves = []
    standings = []

    state = State.START
    audio_state = audio.State.NONE

    # start menu music
    music = audio.MenuMusic()
    music.play()
    audio_state = audio.State.MENU

    # infinite loop (until user exits)
    while state != State.EXIT:
        # events
        events = pygame.event.get()

        # check for exit
        for event in events:
            if event.type == pygame.QUIT:
                state = State.EXIT
                break

        # start menu
        if state == State.START:
            start_menu = menu.Start(config)
            start_menu.render(display)
            start_menu.handle_events(events)
            if start_menu.next:
                state = State.SETUP

        # setup
        elif state == State.SETUP:
            if audio_state != audio.State.MENU:
                music = audio.MenuMusic()
                music.play()
                audio_state = audio.State.MENU

            if len(config_curves) != 4:
                config_curves = []

                mike = curve.ConfigCurve(config, "Mike", color.name_to_rgb("lightblue"), pygame.K_1, pygame.K_LEFT, "LEFT ARROW", pygame.K_RIGHT, "RIGHT ARROW")
                config_curves.append(mike)

                fred = curve.ConfigCurve(config, "Fred", color.name_to_rgb("orange"), pygame.K_2, pygame.K_n, "N", pygame.K_m, "M")
                config_curves.append(fred)

                zig = curve.ConfigCurve(config, "Zig", color.name_to_rgb("lightgreen"), pygame.K_3, pygame.K_d, "D", pygame.K_f, "F")
                config_curves.append(zig)

                jeff = curve.ConfigCurve(config, "Jeff", color.name_to_rgb("red"), pygame.K_4, pygame.K_q, "Q", pygame.K_w, "W")
                config_curves.append(jeff)

            setup_menu = menu.Setup(config, config_curves)
            setup_menu.render(display)
            config_curves = setup_menu.handle_events(events)
            if setup_menu.next:
                curves = setup_menu.get_curves()
                state = State.PLAY

        # play
        elif state == State.PLAY:
            if audio_state != audio.State.GAME:
                music = audio.GameMusic()
                music.play()
                audio_state = audio.State.GAME

            board = game.Game(config, curves, standings)
            board.render(display)
            board.handle_events(events)
            (curves, standings) = board.update()
            if board.is_end:
                state = State.END

        # end
        elif state == State.END:
            end_menu = menu.End(config, curves, standings)
            end_menu.render(display)
            end_menu.handle_events(events)
            if end_menu.next:
                config_curves = []
                curves = []
                standings = []
                state = State.SETUP

        # check for exit
        elif state == State.EXIT:
            break

        # update
        pygame.display.update()

        # keep set frames per second
        clock.tick(config["GAME"]["FPS"])

    pygame.quit()
    quit()
