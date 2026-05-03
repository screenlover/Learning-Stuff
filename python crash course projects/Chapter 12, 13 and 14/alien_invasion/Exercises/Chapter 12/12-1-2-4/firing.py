import pygame
from pygame.sprite import Sprite

class Fire(Sprite):

    def __init__(self, bs_game):
        super().__init__()
        self.screen = bs_game.screen
        self.color = (230,30, 5)

        self.rect = pygame.Rect(0, 0, 15, 4)
        self.rect.center = bs_game.noia.rect.center

        self.x = float(self.rect.x)

    def update(self):
        self.x += 10
        self.rect.x = self.x

    def light_joint(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
