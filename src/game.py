import webcolors as color
import pygame

class Game:
    def __init__(self, config, curves, standings):
        self.config = config
        self.elements = []
        self.curves = curves
        self.standings = standings
        self.is_end = False
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                for curve in self.curves:
                    if event.key == curve.leftKey:
                        curve.left_down()

                    elif event.key == curve.rightKey:
                        curve.right_down()

            elif event.type == pygame.KEYUP:
                for curve in self.curves:
                    if event.key == curve.leftKey:
                        curve.left_up()

                    elif event.key == curve.rightKey:
                        curve.right_up()

    def update(self):        
        for curve in self.curves:
            if (curve.x < 0) or (curve.x > self.config["SCREEN"]["WIDTH"]) or (curve.y < 0) or (curve.y > self.config["SCREEN"]["HEIGHT"]):
                curve.alive = False
            
            elif curve.alive:
                all = [[curve.x, curve.y]]

                for i in range((self.config["CURVE"]["WIDTH"] + 3)):
                    all.append([curve.x + i, curve.y])
                    all.append([curve.x, curve.y + i])
                    all.append([curve.x + i, curve.y + i])
                    all.append([curve.x - i, curve.y])
                    all.append([curve.x, curve.y - i])
                    all.append([curve.x - i, curve.y - i])
                    all.append([curve.x + i, curve.y - i])
                    all.append([curve.x - i, curve.y + i])

                print("ALL")
                print(all)
                print("PATH")
                print(curve.path)

                for point in all:
                    if curve.path.count(point) > 1:
                        curve.alive = False
                        break
                    
                    for other in self.curves:
                        if other.name != curve.name:
                            if point in other.path:
                                curve.alive = False
                                break
            
            if curve.alive:
                curve.update()
            
            else:
                if curve not in self.standings:
                    self.standings.append(curve)

            if len(self.standings) + 1 == len(self.curves):
                self.is_end = True

        return (self.curves, self.standings)

    def render(self, display):
        display.fill(color.name_to_rgb("white"))

        for curve in self.curves:
            curve.render(display)

        for element in self.elements:
            element.render(display)
