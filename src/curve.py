import os
import random
import math
import yaml

with open(os.path.dirname(__file__) + "/../config/config.yml", "r") as yml:
  config = yaml.load(yml)

class Curve:
  def __init__(self, leftKey, rightKey, color):
    self.x = random.randint(50, config["SCREEN"]["WIDTH"] - 50)
    self.y = random.randint(50, config["SCREEN"]["HEIGHT"] - 50)
    self.angle = random.randint(0, 359)
    self.speed = config["GAME"]["SPEED"]
    self.leftKey = leftKey
    self.leftKeyDown = False
    self.rightKey = rightKey
    self.rightKeyDown = False
    self.width = config["CURVE"]["WIDTH"]
    self.color = color
    self.path = [[self.x, self.y]]

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

  def get_coordinates(self):
    return [self.get_x(), self.get_y()]

  def get_path(self):
    return self.path

  def get_width(self):
    return self.width

  def get_color(self):
    return self.color

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
