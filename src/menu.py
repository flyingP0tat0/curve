import webcolors as color
import pygame

import text
import geometry
import curve

class Menu:
    def __init__(self, background, elements = [], curves = []):
        self.background = background
        self.elements = elements
        self.next = False
    
    def enter(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.enter()

    def render(self, display):
        display.fill(self.background)

        for element in self.elements:
            element.render(display)


class Start(Menu):
    def __init__(self, config):
        self.elements = []

        title = "Curve"
        titleText = text.ExoTextBold([config["SCREEN"]["WIDTH"] / 2 - 250, 200], title, 200, color.name_to_rgb("white"))
        instruction = "Press Enter to continue"
        instructionText = text.MuliText([config["SCREEN"]["WIDTH"] / 2 - 150, 500], instruction, 30, color.name_to_rgb("white"))

        self.elements.append(titleText)
        self.elements.append(instructionText)

        Menu.__init__(self, color.name_to_rgb("black"), self.elements)

    def enter(self):
        self.next = True


class Setup(Menu):
    def __init__(self, config, config_curves):
        self.config_curves = config_curves
        self.elements = []

        title = "Setup"
        titleText = text.ExoTextBold([config["SCREEN"]["WIDTH"] / 2 - 75, 0], title, 60, color.name_to_rgb("black"))
        instruction = "Press Enter to continue"
        instructionText = text.MuliText([config["SCREEN"]["WIDTH"] / 2 - 150, config["SCREEN"]["HEIGHT"] - 50], instruction, 30, color.name_to_rgb("black"))

        self.elements.append(titleText)
        self.elements.append(instructionText)

        y = 0

        for player in self.config_curves:
            if player.active:
                box = geometry.Rect([150, 175 + y], 50, 50, player.color, True)

                keysText = player.leftKeyName
                keysText += " + "
                keysText += player.rightKeyName
                keys = text.MuliTextBold([500, 181 + y], keysText, 25, color.name_to_rgb("black"))
                self.elements.append(keys)

            else:
                box = geometry.Rect([150, 175 + y], 50, 50, color.name_to_rgb("grey"), True)

            self.elements.append(box)

            name = text.MuliTextBold([275, 181 + y], player.name, 25, color.name_to_rgb("black"))
            self.elements.append(name)

            y += 125

        Menu.__init__(self, color.name_to_rgb("white"), self.elements)

    def get_curves(self):
        curves = []

        for config_curve in self.config_curves:
            if config_curve.active:
                curves.append(config_curve.to_curve())

        return curves

    def enter(self):
        self.next = True

    def handle_events(self, events):
        Menu.handle_events(self, events)
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                for config_curve in self.config_curves:
                    if event.key == config_curve.toggleKey:
                        config_curve.toggle()
                
                i = 0
                for config_curve in self.config_curves:
                    if config_curve.active:
                        i += 1
                
                if i < 2:
                    for config_curve in self.config_curves:
                        config_curve.active = True

        return self.config_curves


class End(Menu):
    def __init__(self, config, curves, standings):
        self.elements = []
        self.curves = curves
        self.standings = standings

        title = "End"
        titleText = text.ExoTextBold([config["SCREEN"]["WIDTH"] / 2 - 60, 0], title, 60, color.name_to_rgb("black"))
        instruction = "Press Enter to restart"
        instructionText = text.MuliText([config["SCREEN"]["WIDTH"] / 2 - 150, config["SCREEN"]["HEIGHT"] - 50], instruction, 30, color.name_to_rgb("black"))

        self.elements.append(titleText)
        self.elements.append(instructionText)

        y = 0
        i = 1

        for curve in self.curves:
            if curve not in self.standings:
                self.standings.append(curve)

        for player in reversed(self.standings):
            box = geometry.Rect([150, 175 + y], 50, 50, player.color, True)
            self.elements.append(box)

            ranking = str(i)
            ranking += "."

            rankingText = text.MuliTextBold([155, 170 + y], ranking, 45, color.name_to_rgb("black"))
            self.elements.append(rankingText)

            name = text.MuliTextBold([275, 181 + y], player.name, 25, color.name_to_rgb("black"))
            self.elements.append(name)

            y += 125
            i += 1
        
        Menu.__init__(self, color.name_to_rgb("white"), self.elements, [])

    
    def enter(self):
        self.next = True
