import pygame

class Effect:
  def __init__(self, file):
    pygame.mixer.music.load(file)
  
  def play():
    pygame.mixer.music.stop()
    pygame.mixer.music.play(0)


class SelectionEffect(Effect):
  def __init__(self):
    Effect.__init__("../audio/selection.wav")


class Music:
  def __init__(self, file):
    pygame.mixer.music.load(file)
  
  def play():
    pygame.mixer.music.stop()
    pygame.mixer.music.play(0)

  def play_infinitely():
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)


class GameMusic(Music):
  def __init__(self):
    Music.__init__("../audio/funkyelement.mp3")


class MenuMusic(Music):
  def __init__(self):
    Music.__init__("../audio/acousticbreeze.mp3")
