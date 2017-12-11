from typing import List

import pygame

class Text:
    def __init__(self, start: List[int], text: str, font, color):
        self.start = start
        self.text = font.render(text, True, color)

    def render(self, display):
        display.blit(self.text, self.start)

class FileText(Text):
    def __init__(self, start, text: str, font: str, size, color):
        font = pygame.font.Font(font, size)
        Text.__init__(self, start, text, font, color)


class ExoText(FileText):
    def __init__(self, start, text: str, size, color):
        FileText.__init__(self, start, text, "../fonts/Exo/regular.ttf", size, color)


class ExoTextLight(FileText):
    def __init__(self, start, text: str, size, color):
        FileText.__init__(self, start, text, "../fonts/Exo/light.ttf", size, color)


class ExoTextBold(FileText):
    def __init__(self, start, text: str, size, color):
        FileText.__init__(self, start, text, "../fonts/Exo/bold.ttf", size, color)


class MuliText(FileText):
    def __init__(self, start, text: str, size, color):
        FileText.__init__(self, start, text, "../fonts/Muli/regular.ttf", size, color)


class MuliTextLight(FileText):
    def __init__(self, start, text: str, size, color):
        FileText.__init__(self, start, text, "../fonts/Muli/light.ttf", size, color)


class MuliTextBold(FileText):
    def __init__(self, start, text: str, size, color):
        FileText.__init__(self, start, text, "../fonts/Muli/bold.ttf", size, color)
