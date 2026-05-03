import pygame
import sys
from enemy import Enemy
from char import Noia
from firing import Fire
from random import randint

class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")
        self.clock = pygame.time.Clock()
        self.noia = Noia(self)

        self.fires = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()

        self._create_enemy_fleet()

    def run_sky(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_key_event(event, True)
                if event.type == pygame.KEYUP:
                    self._check_key_event(event, False)
            self.screen.fill((40, 40, 250))
            self.noia.update()
            self.noia.blitme()
            self.fires.update()
            for fire in self.fires.sprites():
                fire.light_joint()
            self.enemies.draw(self.screen)
            for fire in self.fires.copy():
                if fire.rect.left >= 800:
                    self.fires.remove(fire)
            for enemy in self.enemies:
                enemy.rect.x -= 1
                if randint(0, 1) and 0 < enemy.rect.y < 600:
                    enemy.rect.y += randint(-10,10)
                
            self._check_joint_collision()
            pygame.display.flip() # renders the next 
            self.clock.tick(60)
    
    def _check_key_event(self, event, flag):
        if event.key == pygame.K_SPACE:
            if flag:
                self._light_joint()
        if event.key == pygame.K_DOWN:
            self.noia.moving_down = flag
        if event.key == pygame.K_UP:
            self.noia.moving_up = flag
        
    def _light_joint(self):
        if len(self.fires) < 1:
            new_joint = Fire(self)
            self.fires.add(new_joint)

    def _create_enemy(self, pos_x, pos_y):
        new_enemy = Enemy(self)
        new_enemy.x = pos_x
        new_enemy.y = pos_y
        new_enemy.rect.x = pos_x
        new_enemy.rect.y = pos_y
        self.enemies.add(new_enemy)

    def _create_enemy_fleet(self):
        enemy = Enemy(self)

        while len(self.enemies) < 6:
            x_coordinate = randint(400, 700)
            y_coordinate = randint(10, 500)
            
            # Prevents enemies from getting grouped together
            for i in self.enemies:
                if x_coordinate - 20 < i.x < x_coordinate + 20 or y_coordinate - 50 < i.y < y_coordinate + 50:
                    break
            else:
                self._create_enemy(x_coordinate, y_coordinate)

    def _check_joint_collision(self):
        collisions = pygame.sprite.groupcollide(
            self.enemies, self.fires, True, True
        )


    

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_sky()