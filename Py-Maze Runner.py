import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Py-Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Player settings
player_size = 20
player_pos = [50, 50]

# Maze settings (walls and exit)
wall_size = 40
walls = [
    pygame.Rect(100, 0, wall_size, 400),
    pygame.Rect(200, 100, wall_size, 300),
    pygame.Rect(300, 0, wall_size, 300),
    pygame.Rect(400, 200, wall_size, 280),
    pygame.Rect(500, 0, wall_size, 150)
]
exit_rect = pygame.Rect(600, 440, wall_size, wall_size)

# Movement speed
speed = 5

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += speed
    if keys[pygame.K_UP]:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += speed

    # Boundary check
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[1] < 0:
        player_pos[1] = 0
    if player_pos[0] > width - player_size:
        player_pos[0] = width - player_size
    if player_pos[1] > height - player_size:
        player_pos[1] = height - player_size

    # Collision with walls
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for wall in walls:
        if player_rect.colliderect(wall):
            # Reset to start if collides with a wall
            player_pos = [50, 50]

    # Check if player reached the exit
    if player_rect.colliderect(exit_rect):
        print("You Win!")
        running = False

    # Draw everything
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, player_rect)  # Draw player
    for wall in walls:
        pygame.draw.rect(window, BLACK, wall)     # Draw walls
    pygame.draw.rect(window, GREEN, exit_rect)   # Draw exit

    # Update display
    pygame.display.flip()
    clock.tick(30)
