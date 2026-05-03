import pygame, sys
from raindrop import RainDrop
from random import randint

class Rain:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rain")
        self.clock = pygame.time.Clock()

        self.rain_drops = pygame.sprite.Group()

        # Create raindrops
        drop = RainDrop(self)
        drop_width = drop.rect.width
        x_axis, y_axis = 0, 0
        while x_axis <= 800:
            new_drop = RainDrop(self)
            new_drop.x = x_axis
            new_drop.y = y_axis
            new_drop.rect.x = x_axis
            new_drop.rect.y = y_axis
            self.rain_drops.add(new_drop)
            x_axis += drop_width

    def rain_init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((2, 10, 30))

            # MaKeItRaIn
            self.rain_drops.draw(self.screen)

            for raindrop in self.rain_drops.sprites():
                raindrop.rect.y += (randint(1,10) + randint(1, 10) + randint(1, 10))/10 

            pygame.display.flip()
            self.clock.tick(60)
    


if __name__ == "__main__":
    rn = Rain()
    rn.rain_init()
