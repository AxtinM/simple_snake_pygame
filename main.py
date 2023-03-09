import pygame
import random

pygame.init()

# Define the window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Create the window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Define the snake properties
SNAKE_BLOCK_SIZE = 10
snake_pos = [250, 250]
snake_body = [[250, 250], [240, 250], [230, 250]]

# Define the food properties
FOOD_BLOCK_SIZE = 10
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

# Update snake position
snake_pos[0] += 10
snake_body.insert(0, list(snake_pos))
snake_body.pop()

# Check for collision with food
if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
    food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
else:
    snake_body.pop()

# Check for collision with the walls or snake body
if snake_pos[0] < 0 or snake_pos[0] > WINDOW_WIDTH - SNAKE_BLOCK_SIZE or snake_pos[1] < 0 or snake_pos[1] > WINDOW_HEIGHT - SNAKE_BLOCK_SIZE or snake_pos in snake_body[1:]:
    game_over = True

# Draw the snake
for block in snake_body:
    pygame.draw.rect(game_window, (0, 255, 0), [block[0], block[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

# Draw the food
pygame.draw.rect(game_window, (255, 0, 0), [food_pos[0], food_pos[1], FOOD_BLOCK_SIZE, FOOD_BLOCK_SIZE])


# Update the display
pygame.display.update()

# Set the game speed
clock = pygame.time.Clock()
clock.tick(10)

