import random
import math
from config import conf

config = conf()

class Curve:
  def __init__(self, leftKey, rightKey, color):
    self.x = random.randint(50, config.WIDTH - 50)
    self.y = random.randint(50, config.HEIGHT - 50)
    self.angle = random.randint(0, 359)
    self.speed = config.SPEED
    self.leftKey = leftKey
    self.rightKey = rightKey
    self.width = config.CURVE_WIDTH
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

  def set_speed(self, speed):
    self.speed = speed

  def left(self):
    self.angle += config.ANGLE_CHANGE

    if self.angle > 359:
      self.angle -= 360

  def right(self):
    self.angle -= config.ANGLE_CHANGE

    if self.angle < 0:
      self.angle += 360

  def move(self, s):
    if self.angle < 90:
      changeX = int(round(s * math.sin(self.angle)))
      changeY = int(round(math.sqrt(s**2 - changeX**2)))

    elif self.angle < 180:
      changeX = int(round(s * math.sin(180 - self.angle)))
      changeY = -1 * int(round(math.sqrt(s**2 - changeX**2)))

    elif self.angle < 270:
      changeX = -1 * int(round(s * math.sin(self.angle - 180)))
      changeY = -1 * int(round(math.sqrt(s**2 - changeX**2)))

    elif self.angle < 360:
      changeX = -1 * int(round(s * math.sin(360 - self.angle)))
      changeY = int(round(math.sqrt(s**2 - changeX**2)))

    self.x += changeX
    self.y += changeY
    self.path.append(self.get_coordinates())

  def update(self):
    self.move(self.speed)
    print(self.angle)
