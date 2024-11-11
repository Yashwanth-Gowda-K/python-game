import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catch the Falling Objects')

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up game variables
basket_width = 100
basket_height = 20
basket_x = (screen_width - basket_width) / 2
basket_y = screen_height - basket_height - 10
basket_speed = 5

falling_object_radius = 20
falling_object_x = random.randint(0, screen_width - falling_object_radius)
falling_object_y = -falling_object_radius
falling_object_speed = 3

score = 0

# Set up font for score
font = pygame.font.SysFont(None, 30)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    # Update falling object position
    falling_object_y += falling_object_speed

    # Check if the object reaches the bottom
    if falling_object_y > screen_height:
        falling_object_x = random.randint(0, screen_width - falling_object_radius)
        falling_object_y = -falling_object_radius

    # Check if the basket catches the falling object
    if (falling_object_y + falling_object_radius > basket_y and
        falling_object_x > basket_x and
        falling_object_x < basket_x + basket_width):
        score += 1
        falling_object_x = random.randint(0, screen_width - falling_object_radius)
        falling_object_y = -falling_object_radius

    # Draw the basket
    pygame.draw.rect(screen, GREEN, (basket_x, basket_y, basket_width, basket_height))

    # Draw the falling object
    pygame.draw.circle(screen, RED, (falling_object_x, falling_object_y), falling_object_radius)

    # Display the score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
