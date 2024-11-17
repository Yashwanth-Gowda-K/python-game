import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game constants
WINDOW_SIZE = 600
TILE_SIZE = 200
GRID_SIZE = 3  # 3x3 grid
EMPTY_TILE = (GRID_SIZE * GRID_SIZE) - 1  # The empty tile position

# Colors
BACKGROUND_COLOR = (50, 50, 50)
TILE_COLOR = (0, 0, 0)  # Black color for tiles
TEXT_COLOR = (255, 255, 255)

# Setup screen
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Sliding Puzzle Game')
font = pygame.font.Font(None, 72)

# Create numbered tiles
tiles = []
for num in range(GRID_SIZE * GRID_SIZE - 1):
    tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile_surface.fill(TILE_COLOR)
    text_surface = font.render(str(num + 1), True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(TILE_SIZE // 2, TILE_SIZE // 2))
    tile_surface.blit(text_surface, text_rect)
    tiles.append(tile_surface)
tiles.append(None)  # The empty tile

# Shuffle the tiles by rearranging their indices
positions = list(range(GRID_SIZE * GRID_SIZE))
random.shuffle(positions)

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // TILE_SIZE, y // TILE_SIZE
            clicked_pos = row * GRID_SIZE + col
            
            # Check if the clicked tile can slide into the empty space
            empty_row, empty_col = positions.index(EMPTY_TILE) // GRID_SIZE, positions.index(EMPTY_TILE) % GRID_SIZE
            if abs(empty_row - row) + abs(empty_col - col) == 1:
                # Swap positions with the empty tile
                positions[positions.index(EMPTY_TILE)], positions[clicked_pos] = positions[clicked_pos], EMPTY_TILE
    
    # Draw tiles
    for idx, pos in enumerate(positions):
        if pos is not EMPTY_TILE:
            tile = tiles[pos]
            row, col = idx // GRID_SIZE, idx % GRID_SIZE
            screen.blit(tile, (col * TILE_SIZE, row * TILE_SIZE))
    
    # Check for win condition
    if positions == list(range(GRID_SIZE * GRID_SIZE)):
        text_surface = font.render("You Win!", True, TEXT_COLOR)
        screen.blit(text_surface, (WINDOW_SIZE // 3, WINDOW_SIZE // 3))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
    
    pygame.display.flip()

pygame.quit()
sys.exit()
