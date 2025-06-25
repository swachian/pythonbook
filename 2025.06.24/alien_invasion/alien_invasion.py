import sys
import pygame
from settings import Settings
from ship import Ship
from joe import Joe
from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.joe = Joe(self)
        self.bullets = pygame.sprite.Group()

        for name in dir(pygame):
            value = getattr(pygame, name)
            if isinstance(value, int):
                print(f"{name} = {value}")

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            print(vars(event))
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.TEXTEDITING:  # 770
                if event.text == 'q':
                    sys.exit()

    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.joe.blitme()

    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()