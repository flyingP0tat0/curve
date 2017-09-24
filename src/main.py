import pygame
from pygame import gfxdraw

import events
import curve
# import menu
# import networking

import threading

from config import conf
from colors import color

config = conf()
color = color()

if __name__ == "__main__":
  pygame.init()

  pygame.display.set_caption("Curve")

  clock = pygame.time.Clock()

  display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

  pygame.display.update()

  curve = curve.Curve(pygame.K_LEFT, pygame.K_RIGHT, color.BLACK)
  curves = [curve]

  exit = False

  while not exit:
    threads = []
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit = True
        break

      thread = threading.Thread(events.handle_event(event, curves))
      thread.start()
      threads.append(thread)

    if exit:
      break

    for thread in threads:
      thread.join()

    display.fill(color.WHITE)

    for curve in curves:
      curve.update()
      pygame.gfxdraw.filled_circle(display, curve.get_x(), curve.get_y(), curve.get_width() + 2, curve.get_color())
      pygame.gfxdraw.aacircle(display, curve.get_x(), curve.get_y(), curve.get_width() + 2, curve.get_color())
      pygame.draw.lines(display, curve.get_color(), False, curve.get_path(), curve.get_width())

    # pygame.gfxdraw.filled_circle(display, head_x, head_y, 5, color.BLACK)
    # pygame.gfxdraw.aacircle(display, head_x, head_y, 5, color.BLACK)
    # pygame.draw.lines(display, color.BLACK, False, my_list, 3)

    pygame.display.update()

    clock.tick(config.FPS)

  pygame.quit()
  quit()
