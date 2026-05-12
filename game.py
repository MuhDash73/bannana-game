import pygame
from settings import *
from debug import debug
from player import Player
from bannana import Bannana
from menus import *

#keep game states, not loop stuff as called every frame, loop is in main

class Game():
    def __init__(self, target_score = 100):
        self.display = pygame.display.get_surface()
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        #self.surface = pygame.display.get_surface()

        self.player = Player(WIDTH//2, HEIGHT//2)
        self.bannanas = pygame.sprite.Group()
        for _ in range(3):
            self.bannanas.add(Bannana(0, 0, self.player, self.bannanas))
        self.target_score = target_score
        self.state = "start_menu"

        #set up visible sprites group and add player and bannana to it
        self.visible_sprites_playing = pygame.sprite.Group()
        self.visible_sprites_playing.add(self.player, self.bannanas)
        self.score = 0
        self.time = 0

        self.menu = StartMenu(self.target_score)
        self.visible_sprites_menu = pygame.sprite.Group()
        self.visible_sprites_menu.add(self.menu.title_sprite, self.menu.start_sprite, self.menu.change_sprite)

        self.end_screen = EndMenu()
        self.end_screen_sprites = pygame.sprite.Group()
        self.end_screen_sprites.add(self.end_screen.title_sprite, self.end_screen.start_sprite, self.end_screen.score_sprite)

        self.clock = pygame.time.Clock()
    
    def scale(self):
        self.display = pygame.display.get_surface()
        self.scaled_surface = pygame.transform.scale(self.surface, self.display.get_size())
        self.display.blit(self.scaled_surface, (0, 0))

        
    def run(self, actual_FPS):
        self.surface.fill("#7BFF66")
        if self.state == "start_menu":
            self.state = self.menu.update()
            self.target_score = self.menu.target_score
            self.visible_sprites_menu.draw(self.surface)

        elif self.state == "playing":
            self.player.update()
            for bannana in self.bannanas:
                if bannana.rect.colliderect(self.player.rect):
                    self.score += 1
                    print(f"collected {self.score} at time {(self.time/FPS):.3f} seconds ({self.time} frames)")
                    debug(f"collected {self.score} at time {(self.time/FPS):.3f} seconds ({self.time} frames)", self.surface, 30, 0)
                
            self.bannanas.update()
            self.visible_sprites_playing.draw(self.surface)
            
            if self.player.started == True:
                self.time += 1
            else:
                self.time = 0
                self.score = 0
                
            debug(f"Score: {self.score}/{self.target_score} FPS: {actual_FPS}/{FPS} Time: {(self.time/FPS):.3f} ({self.time})", self.surface, 0 ,0)
            if self.score >= self.target_score:
                self.state = "game_done"

        elif self.state == "game_done":
            self.end_screen.update(self.time, self.target_score)
            self.end_screen_sprites.draw(self.surface)
        
        self.scale()
