from typing import List

import threading

import pygame

from geometry import *

class Button(Rect):
  def __init__(self, start: List[int], width: int, height: int, width: int, text, color: List[int]):
    self.color = color
    self.text = text

    Rect.__init__(start, width, height, color, 1, True)

  def render(self, display):
    threads = []

    threads += Rect.render(display)
    threads += self.text.render(display)

    return threads
