import pygame

class Joe:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/joe.bmp')
        self.resized_image = pygame.transform.scale(self.image, (120, 100))
        
        self.rect = self.resized_image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.resized_image, self.rect)