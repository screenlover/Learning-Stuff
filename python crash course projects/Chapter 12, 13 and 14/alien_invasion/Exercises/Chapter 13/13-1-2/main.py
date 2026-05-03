import pygame
import sys
from stars import Star
import random

class Sky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Night Sky")
        self.clock = pygame.time.Clock()

        self.stars = pygame.sprite.Group()

        self._create_stars()

    def run_instance(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((13, 15, 59))
            self.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = 0, 0
        while current_y < 600:
            while current_x < 800:
                new_star = Star(self) 
                new_star.x = current_x
                new_star.y = current_y
                new_star.rect.x = current_x
                new_star.rect.y = current_y
                if bool(random.getrandbits(1)):
                    self.stars.add(new_star)
                current_x += star_width
            current_x = 0
            current_y += star_height

if __name__ == "__main__":
    star_sky = Sky()
    star_sky.run_instance()