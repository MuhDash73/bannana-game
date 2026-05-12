import pygame
from settings import *
from debug import debug

class StartMenu():
    def __init__(self, target_score = 100):
        self.font = pygame.font.SysFont("comicsans", 30)

        self.title_surf = self.font.render("Bannana Game", True, "Black")
        self.title_rect = self.title_surf.get_rect(center = (WIDTH//2, HEIGHT//2 - 50))
        self.title_sprite = pygame.sprite.Sprite()
        self.title_sprite.image = self.title_surf
        self.title_sprite.rect = self.title_rect


        self.start_surf = self.font.render("Press Space to Start", True, "Black")
        self.start_rect = self.start_surf.get_rect(center = (WIDTH//2, HEIGHT//2 + 50))
        self.start_sprite = pygame.sprite.Sprite()
        self.start_sprite.image = self.start_surf
        self.start_sprite.rect = self.start_rect
        
        self.font_two = pygame.font.SysFont("comicsans", 10)
        self.target_score = target_score
        self.target_score_cooldown = 0
        self.change_surf = self.font_two.render(f"Arrow keys to change bannana target. current target: {self.target_score}", True, "Black")
        self.change_rect = self.change_surf.get_rect(center = (WIDTH//2, HEIGHT//2 + 150))
        self.change_sprite = pygame.sprite.Sprite()
        self.change_sprite.image = self.change_surf
        self.change_sprite.rect = self.change_rect
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            return "playing"
        
        elif keys[pygame.K_UP] and self.target_score_cooldown == 0:
            self.target_score += 10
            self.target_score_cooldown = 5
            
        elif keys[pygame.K_DOWN] and self.target_score_cooldown == 0:
            self.target_score -= 10
            self.target_score_cooldown = 5
        
        self.target_score = max(10, min(self.target_score, 1000))
        
        self.change_sprite.image = self.font_two.render(f"Arrow keys to change bannana target, current target: {self.target_score}", True, "Black")
        self.target_score_cooldown = max(0, self.target_score_cooldown - 1)
        return "start_menu"

class EndMenu():
    def __init__(self):
        self.font = pygame.font.SysFont("comicsans", 30)

        self.title_surf = self.font.render("You Win!", True, "Black")
        self.title_rect = self.title_surf.get_rect(center = (WIDTH//2, HEIGHT//2 - 50))
        self.title_sprite = pygame.sprite.Sprite()
        self.title_sprite.image = self.title_surf
        self.title_sprite.rect = self.title_rect

        self.start_surf = self.font.render("Press R to Restart", True, "Black")
        self.start_rect = self.start_surf.get_rect(center = (WIDTH//2, HEIGHT//2 + 50))
        self.start_sprite = pygame.sprite.Sprite()
        self.start_sprite.image = self.start_surf
        self.start_sprite.rect = self.start_rect

        self.font_two = pygame.font.SysFont("comicsans", 10)
        self.score_surf = self.font_two.render(f"You got bannanas in", True, "Black")
        self.score_rect = self.score_surf.get_rect(center = (WIDTH//2, HEIGHT//2 + 150))
        self.score_sprite = pygame.sprite.Sprite()
        self.score_sprite.image = self.score_surf
        self.score_sprite.rect = self.score_rect

    def update(self, time, target_score):
        self.score_sprite.image = self.font_two.render(f"You got {target_score} bannanas in {(time/FPS):.3f} seconds ({time} frames)", True, "Black")
        self.score_sprite.rect = self.score_sprite.image.get_rect(center = (WIDTH//2, HEIGHT//2 + 150))