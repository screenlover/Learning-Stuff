import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        
        self.image = pygame.image.load("yui.bmp")
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.rect.size

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    