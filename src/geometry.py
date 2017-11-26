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
    return [threading.Thread(pygame.gfxdraw.pixel(display, self.x, self.y, self.color))]


class Line:
  def __init__(self, start: List[int], end: List[int], color: List[int], width: int = 1):
    self.start = start
    self.end = end
    self.color = color
    self.width = width

  def render(self, display):
    return [threading.Thread(pygame.draw.line(display, self.color, self.start, self.end, self.width))]


class Path:
  def __init__(self, points: List[List[int]], color: List[int], width: int = 1):
    self.points = points
    self.color = color
    self.width = width

  def render(self, display):
    threads = []

    if len(self.points) > 0:

      i = 0

      for point in self.points:
        if len(self.points) > i + 1:
          i += 1
          start = point
          end = self.points[i]
          line = Line(start, end, self.color, self.width)
          threads += line.render(display)

    return threads


class Rect(Path):
  def __init__(self, start: List[int], width: int, height: int, color: List[int], lines_width: int = 1, filled: bool = False):
    self.start = start
    self.width = width
    self.height = height
    self.filled = filled

    a_start = [start[0], start[1]]
    a_end = [start[0] + width, start[1]]
    a = [a_start, a_end]

    c = [[a_start[0], a_start[1] + height], [a_end[0], a_end[1] + height]]

    b_start = a_end
    b_end = [a_end[0], a_end[1] + height]
    b = [b_start, b_end]

    Path.__init__([a[0], a[1], b[0], b[1], c[0], c[1], c[0], a[0]], color, lines_width)

  def render(self, display):
    return Path.render(display)

  def on_click(self, function):
    self.on_click = function

  def click(self, x, y):
    if x >= self.start[0] and x <= self.start[0] + self.width:
      self.on_click()

    if y >= self.start[1] and y <= self.start[1] + self.height:
      self.on_click()


class Circle:
  def __init__(self, centre: List[int], radius: int, color: List[int], width: int = 0, filled: bool = False):
    self.centre = centre
    self.radius = radius
    self.color = color
    self.width = width
    self.filled = filled

  def render(self, display):
    threads = []

    if self.filled:
      threads.append(threading.Thread(pygame.gfxdraw.filled_circle(display, self.centre[0], self.centre[1], self.radius, self.color)))
      self.width = 0

    if self.width == 0:
      threads.append(threading.Thread(pygame.gfxdraw.aacircle(display, self.centre[0], self.centre[1], self.radius, self.color)))

    else:
      threads.append(threading.Thread(pygame.draw.circle(display, self.color, [self.centre[0], self.centre[1]], self.radius, self.width)))

    return threads

  def on_click(self, function):
    self.on_click = function

  def click(self, x, y):
    if (x - self.centre[0])**2 + (y - center[1])**2 < self.radius**2:
      self.on_click()
