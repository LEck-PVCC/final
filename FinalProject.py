import pygame
import random

pygame.init()

# Screen dimensions
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Clock & font
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

# Snake block size & speed
block_size = 20
speed = 10

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, pos)

def gameLoop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake =[]
    length = 1

    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

# Gameover / retry
    while not game_over:
        while game_close:
            win.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red, [50, height // 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

# Key comands
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = block_size

        x += x_change
        y += y_change

# Wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

# Snake & food
        win.fill(black)
        pygame.draw.rect(win, green, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        for block in snake:
            pygame.draw.rect(win, white, [block[0], block[1], block_size, block_size])

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()
