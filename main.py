import pygame
import sys
from core import Snake, Field, Food


WIDTH = 600
HEIGHT = 600
FPS = 60


WHITE = (255, 255, 255)
GREY = (41, 49, 51)
GREEN = (68, 148, 74)
PURPLE = (20, 0, 66)
YELLOW = (240, 215, 81)
RED = (227, 38, 54)

class App():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        self.snake = Snake()
        self.snake_sprites = pygame.sprite.Group(self.snake)

        self.food = Food()
        self.food_sprites = pygame.sprite.Group(self.food)

        self.field = Field()
        self.field_sprites = pygame.sprite.Group(self.field)

        self.running_app = True


    def running(self):
        while self.running_app == True:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running_app = False


    def update(self):
        self.all_sprites.update()
        self.snake_sprites.update()


    def draw(self):
        self.screen.fill(PURPLE)
        self.field_sprites.draw(self.screen)
        self.snake_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    app = App()
    app.running()
