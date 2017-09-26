import pygame

def handle_event(event, curves):
  for curve in curves:
    if event.type == pygame.KEYDOWN:
      if event.key == curve.leftKey:
         curve.left_down()

      elif event.key == curve.rightKey:
        curve.right_down()

    elif event.type == pygame.KEYUP:
      if event.key == curve.leftKey:
         curve.left_up()

      elif event.key == curve.rightKey:
        curve.right_up()
