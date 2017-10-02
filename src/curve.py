import os
import random
import math

import pygame
from pygame import gfxdraw

import util

config = util.get_config("config.yml")

class Curve:
  def __init__(self, name, color, leftKey, rightKey):
    self.name = name
    self.color = color
    self.x = random.randint(50, config["SCREEN"]["WIDTH"] - 50)
    self.y = random.randint(50, config["SCREEN"]["HEIGHT"] - 50)
    self.angle = random.randint(0, 359)
    self.speed = config["GAME"]["SPEED"]
    self.leftKey = leftKey
    self.leftKeyDown = False
    self.rightKey = rightKey
    self.rightKeyDown = False
    self.width = config["CURVE"]["WIDTH"]
    self.path = [[self.x, self.y]]

  def get_coordinates(self):
    return [self.x, self.y]

  def left_down(self):
    self.leftKeyDown = True

  def right_down(self):
    self.rightKeyDown = True

  def left_up(self):
    self.leftKeyDown = False

  def right_up(self):
    self.rightKeyDown = False

  def set_speed(self, speed):
    self.speed = speed

  def move(self, s):
    self.x += int(s * math.cos(self.angle * math.pi / 180))
    self.y += int(s * math.sin(self.angle * math.pi / 180))
    self.path.append(self.get_coordinates())

  def update(self):
    if self.leftKeyDown:
      self.angle -= config["CURVE"]["ANGLE_CHANGE"]

      if self.angle < 0:
        self.angle += 360

    if self.rightKeyDown:
      self.angle += config["CURVE"]["ANGLE_CHANGE"]

      if self.angle > 359:
        self.angle -= 360

    self.move(self.speed)

  def render(self, display):
    pygame.gfxdraw.filled_circle(display, self.x, self.y, self.width + 2, self.color)
    pygame.gfxdraw.aacircle(display, self.x, self.y, self.width + 2, self.color)
    pygame.draw.lines(display, self.color, False, self.path, self.width)
