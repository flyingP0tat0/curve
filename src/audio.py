from enum import Enum
import os

import pygame

import util

root = util.get_root()

class State(Enum):
    NONE = 0
    MENU = 1
    GAME = 2
    SELECTION = 3


class Music:
    def __init__(self, file):
        pygame.mixer.music.load(file)

    def play(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(0)

    def play_infinitely(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)


class GameMusic(Music):
    def __init__(self):
        Music.__init__(self, os.path.join(root, "audio/funkyelement.mp3"))


class MenuMusic(Music):
    def __init__(self):
        Music.__init__(self, os.path.join(root, "audio/acousticbreeeze.mp3"))
