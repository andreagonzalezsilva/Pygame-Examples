import math
import random
import sys
import pygame
from pygame.locals import *

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_caption("Cool Lines")

        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()
        self.screen_res = [640, 480]

        self.circles = []

        # pygame.HWSURFACE is deprecated/ignored in SDL2; passing standard display mode
        self.screen = pygame.display.set_mode(self.screen_res)

        self.createCircles()

        while True:
            self.Loop()

    def Loop(self):
        self.eventLoop()
        self.Tick()
        self.Draw()
        pygame.display.update()

    def createCircles(self):
        # circle item format: [pos, vector]
        for _ in range(100):
            pos = [320.0, 240.0]
            vector = self.getVector()
            self.circles.append([pos, vector])

    def getDistance(self, pos1, pos2):
        return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1])

    def getVector(self):
        speed = 5.0
        distance = [random.randrange(-40, 40) / 10.0, random.randrange(-40, 40) / 10.0]

        try:
            norm = math.hypot(distance[0], distance[1])
            direction = [distance[0] / norm, distance[1] / norm]
            vector = [direction[0] * speed, direction[1] * speed]
        except ZeroDivisionError:
            vector = [speed, speed]

        return vector

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def Tick(self):
        self.ttime = self.clock.tick(60)

    def Draw(self):
        self.screen.fill((0, 0, 0))

        for circle in self.circles:
            circle[0][0] += circle[1][0]
            circle[0][1] += circle[1][1]

            if circle[0][0] > 640 or circle[0][0] < 0:
                circle[1][0] *= -1

            elif circle[0][1] > 480 or circle[0][1] < 0:
                circle[1][1] *= -1

            for c in self.circles:
                dist = self.getDistance(circle[0], c[0])
                if dist < 175:
                    pygame.draw.line(self.screen, (255, 0, 0), circle[0], c[0])
                elif dist < 200:
                    pygame.draw.line(self.screen, (0, 0, 255), circle[0], c[0])
                elif dist < 225:
                    pygame.draw.line(self.screen, (0, 255, 0), circle[0], c[0])


if __name__ == "__main__":
    Game()