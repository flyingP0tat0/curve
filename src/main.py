import os
import threading
import yaml

import pygame

import events
import curve
import draw
# import menu
# import audio
# import networking

# setup config
with open(os.path.dirname(__file__) + "/../config/config.yml", "r") as yml:
  config = yaml.load(yml)

#setup colors
with open(os.path.dirname(__file__) + "/../config/color.yml", "r") as yml:
  color = yaml.load(yml)

# convert dicts to RGBs
for colorName in color:
  color[colorName] = (color[colorName]["R"], color[colorName]["G"], color[colorName]["B"], color[colorName]["A"])
  
# main function
if __name__ == "__main__":
  pygame.init()

  pygame.display.set_caption("Curve")

  clock = pygame.time.Clock()

  # set window size
  display = pygame.display.set_mode((config["SCREEN"]["WIDTH"], config["SCREEN"]["HEIGHT"]))

  pygame.display.update()

  # create curves
  curve = curve.Curve(pygame.K_LEFT, pygame.K_RIGHT, color["BLACK"])
  curves = [curve]

  exit = False

  # infinite loop (until user exits)
  while not exit:
    threads = []
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit = True
        break

      # thread for every event
      thread = threading.Thread(events.handle_event(event, curves))
      thread.start()
      threads.append(thread)

    if exit:
      break

    # wait for event threads to finish before going on
    for thread in threads:
      thread.join()

    # clear screen
    display.fill(color["WHITE"])

    # draw every curve
    for curve in curves:
      curve.update()
      draw.curve(display, curve)

    pygame.display.update()

    # keep set frames per second
    clock.tick(config["GAME"]["FPS"])

  pygame.quit()
  quit()
