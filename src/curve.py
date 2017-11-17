import os
import random
import math

import pygame
from pygame import gfxdraw

import util
import geometry

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
    self.path.append([self.x, self.y])

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
    threads = []

    head = geometry.Circle([200, 200], 100, self.color, self.width + 2, True)
    threads += head.render(display)

    path = geometry.Path(self.path, self.color, self.width)
    threads += path.render(display)

    return threads
