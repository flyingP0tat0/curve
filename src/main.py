import threading

import pygame
import webcolors as color

# import audio
# import collision
# import components
import curve
import events
# import menu
# import networking
import util

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

  # create curves
  curve = curve.Curve("Jan", color.name_to_rgb("black"), pygame.K_LEFT, pygame.K_RIGHT)
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
    display.fill(color.name_to_rgb("white"))

    # draw every curve
    for curve in curves:
      curve.update()
      curve.render(display)

    pygame.display.update()

    # keep set frames per second
    clock.tick(config["GAME"]["FPS"])

  pygame.quit()
  quit()
