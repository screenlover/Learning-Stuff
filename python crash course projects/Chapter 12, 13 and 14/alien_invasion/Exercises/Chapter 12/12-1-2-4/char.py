import pygame
class Noia:
    def __init__(self, bs_game):
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()
        
        self.image = pygame.image.load("noia.bmp")
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = self.moving_left = self.moving_up = self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - 500:
            self.x += 2
        if self.moving_left and self.rect.left > 0:
            self.x -= 2  
        if self.moving_up and self.rect.top > 0:
            self.y -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom + 50:
            self.y += 2

        self.rect.x = self.x
        self.rect.y = self.y      

    def blitme(self):
        self.screen.blit(self.image, self.rect)