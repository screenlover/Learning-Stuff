import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ss_screen):
        super().__init__()
        self.screen = ss_screen.screen

        self.image = pygame.image.load("star.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)