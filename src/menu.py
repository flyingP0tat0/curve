import threading

import webcolors as color

import components

class Menu:
  def __init__(self, display, background, elements):
    self.background = background
    self.display = display
    self.elements = elements
  
  def render(self, display):
    self.display.fill(background)

    for element in self.elements:
      element.render(display)


class Start(Menu):
  def __init__(self):
    self.title = "Curve"
    Menu.__init__(display, color.name_to_rgb("black"))


class Main(Menu):
  def __init__(self, display):
    self.title = "Main"
    Menu.__init__(display, color.name_to_rgb("black"))


class Pause(Menu):
  def __init__(self, display):
    self.title = "Pause"
    Menu.__init__(display, color.name_to_rgb("black"))


class End(Menu):
  def __init__(self, display):
    self.title = "End"
    Menu.__init__(display, color.name_to_rgb("black"))


class Settings(Menu):
  def __init__(self, display):
    self.title = "Settings"
    Menu.__init__(display, color.name_to_rgb("black"))
