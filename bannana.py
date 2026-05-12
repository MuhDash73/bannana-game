import pygame
from settings import *
from debug import debug
import random

class Bannana(pygame.sprite.Sprite):
    def __init__(self, x, y, player, bannana_group):
        super().__init__()
        self.image = pygame.image.load("assets/bannana.png").convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.player = player
        self.leniency = 50
        self.teleport()
    
    def teleport(self):
        self.rect.x = random.randrange(10, WIDTH - self.leniency, self.leniency)
        self.rect.y = random.randrange(10, HEIGHT - self.leniency, self.leniency)
    
    def update(self):
        while self.rect.colliderect(self.player.rect) or any(self.rect.colliderect(bannana.rect) for bannana in self.groups()[0] if bannana != self):
            self.teleport()