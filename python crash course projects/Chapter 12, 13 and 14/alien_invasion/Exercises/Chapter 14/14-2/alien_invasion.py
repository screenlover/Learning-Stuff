import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button

class AlienInvasion:
    
    def __init__(self):
        """Initializes the game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Draws the display window according to the dimensions passed in the tuple
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update() # will update the ship's position for each pass through the loop
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)  # the while loop will run about 60 times per second

    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            pygame.mouse.set_visible(True)
            self.game_active = False
        
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        self.settings.fleet_direction *= -1
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.x > self.screen.get_width():
                self.bullets.remove(bullet)
                self._ship_hit()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
    
    def _check_events(self): # helper methods are not meant to be used outside the class and always start with an underscore
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q): # simpler and cleaner than the original solution (i guess...)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_event(event, True)
            elif event.type == pygame.KEYUP:
                self._check_key_event(event, False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)        

    def _start_game(self):
        if not self.game_active:
            self.stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            self._start_game()
            
    def _check_key_event(self, event, flag): # checking for a general key event with a "True" flag for down and "False" for up is better than dividing it into two functions, that is, it's better than the original solution
        """Checks for a general key event. When the flag is True the 'moving' event triggered, otherwise it is cancelled."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = flag
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = flag
        if event.key == pygame.K_SPACE and event.type == pygame.KEYDOWN:
            self._fire_bullet()
        if event.key == pygame.K_p:
            self._start_game()
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) # Redraws the screen with the given bg_color
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = self.screen.get_width() - 2 * alien_width, alien_height
        self._create_alien(current_x, current_y)
        current_x += 2 * alien_width
        current_x = alien_width
        current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
