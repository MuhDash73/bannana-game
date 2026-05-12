import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.x_speed = 0
        self.y_speed = 0
        self.acceleration = 1
        self.started = False
    
    def move(self):
        keys = pygame.key.get_pressed()

        self.left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        self.right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        self.up = keys[pygame.K_w] or keys[pygame.K_UP]
        self.down = keys[pygame.K_s] or keys[pygame.K_DOWN]

        if self.left:
            self.x_speed -= self.acceleration
        if self.right:
            self.x_speed += self.acceleration
        if self.up:
            self.y_speed -= self.acceleration
        if self.down:
            self.y_speed += self.acceleration
        
        if self.left or self.right or self.up or self.down:
             self.started = True
        
        self.x_speed *= 0.9
        self.y_speed *= 0.9
        
        self.rect.x += self.x_speed
        self.old_x = self.rect.x
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        if self.rect.x != self.old_x:
            self.x_speed = 0
        self.rect.y += self.y_speed
        self.old_y = self.rect.y
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))
        if self.rect.y != self.old_y:
            self.y_speed = 0

        if self.x_speed != 0 or self.y_speed != 0:
            self.started = True

    def update(self):
        self.move()