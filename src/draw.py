import pygame
from pygame import gfxdraw

def curve(display, curve):
  pygame.gfxdraw.filled_circle(display, curve.get_x(), curve.get_y(), curve.get_width() + 2, curve.get_color())
  pygame.gfxdraw.aacircle(display, curve.get_x(), curve.get_y(), curve.get_width() + 2, curve.get_color())
  pygame.draw.lines(display, curve.get_color(), False, curve.get_path(), curve.get_width())
