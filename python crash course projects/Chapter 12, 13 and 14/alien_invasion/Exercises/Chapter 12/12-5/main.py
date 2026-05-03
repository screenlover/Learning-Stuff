import pygame
import sys

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Keys")
        self.clock = pygame.time.Clock()

        self.char = Char(self)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.dict['unicode'] != '':
                        self.char.image = pygame.font.SysFont(None, 120).render(event.dict['unicode'], True, (255, 255, 255))
            self.screen.fill((50, 50, 50))
            self.char.blitme()
            pygame.display.flip()


class Char:
    def __init__(self, key_game):
        self.screen = key_game.screen
        self.screen_rect = key_game.screen.get_rect()

        self.image = pygame.font.SysFont(None, 120).render(".", True, (255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)



if __name__ == '__main__':
    mg = Keys()
    mg.run_game()
