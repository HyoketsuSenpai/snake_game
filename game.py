import sys
import pygame
import random
from pygame.math import Vector2


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.wrap()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def wrap(self):
        if not 0 <= self.snake.body[0].x:
            self.snake.body[0].x = 19
        if not self.snake.body[0].x < cell_number:
            self.snake.body[0].x = 0
        if not 0 <= self.snake.body[0].y:
            self.snake.body[0].y = 19
        if not self.snake.body[0].y < cell_number:
            self.snake.body[0].y = 0


class SNAKE:

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (133, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body
            self.new_block = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    def add_block(self):
        self.new_block = True


class FRUIT:

    def __init__(self):
        self.randomize()
        self.apple = pygame.image.load('assets/apple.png').convert_alpha()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
frame_rate = 60

main_game = MAIN()
is_running = True

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction != (0, 1):
                main_game.snake.direction = (0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction != (0, -1):
                main_game.snake.direction = (0, 1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction != (-1, 0):
                main_game.snake.direction = (1, 0)
            if event.key == pygame.K_LEFT and main_game.snake.direction != (1, 0):
                main_game.snake.direction = (-1, 0)
    screen.fill((175, 215, 70))
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(frame_rate)
