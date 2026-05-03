import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
    
    def __init__(self, rain_sim):
        super().__init__()
        self.screen = rain_sim.screen
        
        self.image = pygame.image.load("raindrop.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    