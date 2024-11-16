import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_size = 20
player_pos = [20, 20]
player_speed = 5

# Maze settings
maze_size = 30  # Number of rows and columns in the maze
cell_size = width // maze_size
maze = []

# Exit settings
exit_pos = []

# Game variables
score = 0
game_over = False
time_left = 30  # 30 seconds to complete the maze
font = pygame.font.Font(None, 36)

def generate_maze():
    """Generate a simple random maze."""
    global exit_pos
    maze.clear()
    for row in range(maze_size):
        maze.append([random.choice([0, 1]) for _ in range(maze_size)])
    
    # Ensure start and exit are open
    maze[0][0] = 0
    exit_pos = [maze_size - 1, maze_size - 1]
    maze[exit_pos[0]][exit_pos[1]] = 0  # Exit is at bottom-right corner

def draw_maze():
    """Draw the maze and exit."""
    for row in range(maze_size):
        for col in range(maze_size):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size), 1)

def draw_player():
    """Draw the player character."""
    pygame.draw.rect(screen, GREEN, (player_pos[0] * cell_size, player_pos[1] * cell_size, player_size, player_size))

def move_player():
    """Move the player based on input."""
    global game_over
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_pos[0] > 0 and maze[player_pos[1]][player_pos[0] - 1] == 0:
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and player_pos[0] < maze_size - 1 and maze[player_pos[1]][player_pos[0] + 1] == 0:
        player_pos[0] += 1
    if keys[pygame.K_UP] and player_pos[1] > 0 and maze[player_pos[1] - 1][player_pos[0]] == 0:
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and player_pos[1] < maze_size - 1 and maze[player_pos[1] + 1][player_pos[0]] == 0:
        player_pos[1] += 1

    # Check if player reached the exit
    if player_pos == exit_pos:
        game_over = True

def draw_timer():
    """Draw the timer countdown."""
    global time_left
    time_text = font.render(f"Time Left: {time_left}", True, RED)
    screen.blit(time_text, (width - 150, 10))

# Game loop
clock = pygame.time.Clock()
generate_maze()  # Generate the maze at the start
start_ticks = pygame.time.get_ticks()  # Track the start time
while True:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Time countdown
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, 30 - seconds)  # Ensure time left doesn't go below 0
    if time_left == 0:
        game_over = True

    # Game logic
    if not game_over:
        move_player()

    # Draw everything
    draw_maze()
    draw_player()
    draw_timer()

    # Game over screen
    if game_over:
        if player_pos == exit_pos:
            game_over_text = font.render("You Win!", True, GREEN)
        else:
            game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (width // 2 - 100, height // 2))

    # Update display
    pygame.display.flip()
    clock.tick(30)
