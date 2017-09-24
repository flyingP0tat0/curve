import pygame

def handle_event(event, curves):
  for curve in curves:
    if event.type == pygame.KEYDOWN:
      if event.key == curve.leftKey:
         curve.left()

      elif event.key == curve.rightKey:
        curve.right()
