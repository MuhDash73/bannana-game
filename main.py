import pygame
import os
from settings import *
from debug import debug
from game import Game

class Main():
    def __init__(self):

        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Bannana Game")
        self.clock = pygame.time.Clock()
        self.fullscreen = False

        self.FPS = FPS
        self.game = Game()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    if self.fullscreen:
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                    else:
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        self.screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.RESIZABLE)
                    self.fullscreen = not self.fullscreen
                    self.game.display = pygame.display.get_surface()
                    print(self.fullscreen)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    temp = self.game.target_score
                    self.game = Game(temp)

            self.actual_FPS = int(self.clock.get_fps())
            self.game.run(self.actual_FPS)
            pygame.display.update()
            self.clock.tick(self.FPS)
        
            



if __name__ == "__main__":
    main = Main()
    main.run()