import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from joe import Joe
from bullet import Bullet
from alien import Alien
from random import randint
from game_stats import GameStats
from button import Button 
from scoreboard import Scoreboard

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.joe = Joe(self)
        self.bullets = pygame.sprite.Group()
    
        self.game_active = False
        
        self.aliens = pygame.sprite.Group()
        # self._create_fleet()
        self.play_button = Button(self, "Play")

        # for name in dir(pygame):
        #     value = getattr(pygame, name)
        #     if isinstance(value, int):
        #         print(f"{name} = {value}")

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            # print(vars(event))
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.TEXTEDITING:  # 770
                if event.text == 'q':
                    sys.exit()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_9 and not self.game_active:
            self._start_game()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self._start_game()

    def _start_game(self):
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)
        self.settings.initialize_dynamic_settings()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        random_max = alien_width/1.5
        while current_y < (self.settings.screen_height - 5 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # self._create_alien(current_x + randint(-1*random_max, random_max), current_y +  randint(-random_max, random_max))
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()

        # self.joe.blitme()
        # print(type(self.screen))
        # print(type(self.aliens))
        self.aliens.draw(self.screen)

    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if self._check_aliens_collide_ship() or self._check_aliens_bottom():
            print("Ship hit!!!")
            self._ship_hit()
    
    def _check_aliens_collide_ship(self):
        return pygame.sprite.spritecollideany(self.ship, self.aliens)

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False
    
    def _ship_hit(self):
        if self.stats.ships_left > 0 :
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()