import pygame


WIDTH = 600
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (68, 148, 74)
PURPLE = (20, 0, 66)
YELLOW = (240, 215, 81)
RED = (227, 38, 54)
GREY = (41, 49, 51)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((GREEN))
        pygame.draw.rect(self.image, BLACK, self.image.get_rect(), 2)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        pass


class Field(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH - 100, HEIGHT - 100))
        self.image.fill((GREY))
        pygame.draw.rect(self.image, BLACK, self.image.get_rect(), 2)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
