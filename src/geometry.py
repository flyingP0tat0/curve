from typing import List

import threading

import pygame
from pygame import gfxdraw

class Point:
  def __init__(self, x: int, y: int, color: List[int]):
    self.x = x
    self.y = y
    self.color = color

  def render(self, display):
    pygame.gfxdraw.pixel(display, self.x, self.y, self.color)


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
    threads = []

    for point in self.points:
      line = Line(point[0], point[1], self.color, self.width)

      thread = threading.Thread(line.render())
      thread.start()
      threads.append(thread)

    for thread in threads:
      thread.join()


class Rect:
  def __init__(self, start: List[int], width: int, height: int, color: List[int], lines_width: int = 1, filled: bool = False):
    self.start = start
    self.width = width
    self.height = height
    self.color = color
    self.lines_width = lines_width
    self.filled = filled

    a_start = [start[0], start[1]]
    a_end = [start[0] + width, start[1]]
    a = [s_start, a_end]

    b_start = a_end
    b_end = [a_end[0], a_end[1] + height]
    b = [b_start, b_end]

    self.path = Path([a, b], self.color, self.lines_width)

  def render(self, display):
    self.path.render(display)

  def on_click(self, function):
    self.on_click = function

  def click(self, x, y):
    if x >= self.start[0] && x <= (self.start[0] + self.width)
      self.on_click()

    if y >= self.start[1] && y <= (self.start[1] + self.height)
      self.on_click()


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

    if self.width = 0:
      pygame.gfxdraw.aacircle(display, self.centre[0], self.centre[1], self.radius, self.color)

    else:
      pygame.draw.circle(display, self.color, [self.centre[0], self.centre[1]], self.radius, self.width)

  def on_click(self, function):
    self.on_click = function

  def click(self, x, y):
    if (x - self.centre[0])**2 + (y - center[1])**2 < self.radius**2
      self.on_click()
