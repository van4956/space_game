import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    def __init__(self, screen):
        """инициальзация пушки/танка"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (8).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - 15
        self.mright = False
        self.mleft = False

    def output(self):
        """отрисовка пушки/танка"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновления позиции пушки/танка"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 4.5
        if self.mleft and self.rect.left > 0:
            self.center -= 4.5
        self.rect.centerx = self.center

    def create_gun(self):
        """размещает танк в центре внизу"""
        self.center = self.screen_rect.centerx