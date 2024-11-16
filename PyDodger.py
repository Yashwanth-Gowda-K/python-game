import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyDodger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [width // 2, height - 2 * player_size]
player_speed = 10

# Obstacle settings
obstacle_size = 50
obstacle_pos = [random.randint(0, width - obstacle_size), 0]
obstacle_speed = 5
obstacles = [obstacle_pos]

# Game variables
score = 0
level = 1
game_over = False

# Font settings
font = pygame.font.Font(None, 36)

def drop_obstacles(obstacles):
    """Add a new obstacle at random x position at the top of the screen."""
    delay = random.random()
    if len(obstacles) < 10 and delay < 0.1:
        x_pos = random.randint(0, width - obstacle_size)
        obstacles.append([x_pos, 0])

def draw_obstacles(obstacles):
    """Draw all obstacles on the screen."""
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

def update_obstacle_positions(obstacles):
    """Move obstacles down the screen, update score if obstacle passed player."""
    global score, game_over
    for obstacle in obstacles:
        if obstacle[1] >= 0 and obstacle[1] < height:
            obstacle[1] += obstacle_speed
        else:
            obstacles.remove(obstacle)
            score += 1

def check_collision(player_pos, obstacles):
    """Check for collision between player and obstacles."""
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_size, obstacle_size)
        if player_rect.colliderect(obstacle_rect):
            return True
    return False

# Game loop
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += player_speed

    # Drop and draw obstacles
    drop_obstacles(obstacles)
    update_obstacle_positions(obstacles)

    # Check for collisions
    if check_collision(player_pos, obstacles):
        game_over = True

    # Increase difficulty with levels
    if score > 10 * level:
        level += 1
        obstacle_speed += 1  # Increase speed each level

    # Game over screen
    if game_over:
        screen.fill(WHITE)
        game_over_text = font.render("Game Over!", True, BLACK)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(game_over_text, (width // 2 - 60, height // 2 - 20))
        screen.blit(score_text, (width // 2 - 60, height // 2 + 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Draw everything
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))  # Player
    draw_obstacles(obstacles)

    # Display score and level
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Update display and set frame rate
    pygame.display.flip()
    clock.tick(30)
