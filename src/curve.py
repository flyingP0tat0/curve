import random
import math

import pygame
from pygame import gfxdraw

import util
import geometry

class ConfigCurve:
    def __init__(self, config, name, color, toggleKey, leftKey, leftKeyName, rightKey, rightKeyName):
        self.active = True
        self.config = config
        self.name = name
        self.color = color
        self.toggleKey = toggleKey
        self.leftKey = leftKey
        self.leftKeyName = leftKeyName
        self.rightKey = rightKey
        self.rightKeyName = rightKeyName
    
    def toggle(self):
        self.active = not self.active
    
    def to_curve(self):
        return Curve(self.config, self.name, self.color, self.leftKey, self.rightKey)


class Curve:
    def __init__(self, config, name, color, leftKey, rightKey):
        self.alive = True
        self.config = config
        self.name = name
        self.color = color
        self.x = random.randint(50, self.config["SCREEN"]["WIDTH"] - 50)
        self.y = random.randint(50, self.config["SCREEN"]["HEIGHT"] - 50)
        self.angle = random.randint(0, 359)
        self.speed = self.config["GAME"]["SPEED"]
        self.leftKey = leftKey
        self.leftKeyDown = False
        self.rightKey = rightKey
        self.rightKeyDown = False
        self.width = self.config["CURVE"]["WIDTH"]
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
            self.angle -= self.config["CURVE"]["ANGLE_CHANGE"]

        if self.angle < 0:
            self.angle += 360

        if self.rightKeyDown:
            self.angle += self.config["CURVE"]["ANGLE_CHANGE"]

        if self.angle > 359:
            self.angle -= 360

        self.move(self.speed)

    def render(self, display):
        head = geometry.Circle([self.x, self.y], self.width + 2, self.color, 0, True)
        head.render(display)

        path = geometry.Path(self.path, self.color, self.width)
        path.render(display)
