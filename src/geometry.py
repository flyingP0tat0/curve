from typing import List

import pygame

class Line:
    def __init__(self, start: List[int], end: List[int], color: List[int], width: int = 1):
        self.start = start
        self.end = end
        self.color = color
        self.width = width

    def render(self, display):
        pygame.draw.line(display, self.color, self.start, self.end, self.width)


class Path:
    def __init__(self, points: List[List[int]], color: List[int], width: int = 1):
        self.points = points
        self.color = color
        self.width = width

    def render(self, display):
        if len(self.points) > 0:
            i = 0

        for point in self.points:
            if len(self.points) > i + 1:
                i += 1

            start = point
            end = self.points[i]
            line = Line(start, end, self.color, self.width)
            line.render(display)


class Rect:
    def __init__(self, start: List[int], width: int, height: int, color: List[int], filled: bool = False):
        self.rect = [start[0], start[1], width, height]
        self.start = start
        self.width = width
        self.height = height
        self.color = color
        self.filled = filled

    def render(self, display):
        if self.filled:
            display.fill(self.color, self.rect)

        else:
            pygame.draw.rect(display, self.color, self.rect)


class Circle:
    def __init__(self, centre: List[int], radius: int, color: List[int], width: int = 0, filled: bool = False):
        self.centre = centre
        self.radius = radius
        self.color = color
        self.width = width
        self.filled = filled

    def render(self, display):
        if self.filled:
            pygame.gfxdraw.filled_circle(display, self.centre[0], self.centre[1], self.radius, self.color)
            self.width = 0

        if self.width == 0:
            pygame.gfxdraw.aacircle(display, self.centre[0], self.centre[1], self.radius, self.color)

        else:
            pygame.draw.circle(display, self.color, [self.centre[0], self.centre[1]], self.radius, self.width)
