import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного врага"""
    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (2).png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width - 1000
        self.rect.y = self.rect.height - 1000
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод врага на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает врагов"""
        self.y += 0.1
        self.rect.y = self.y