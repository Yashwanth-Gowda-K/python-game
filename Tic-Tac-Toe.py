import pygame
import sys

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
LINE_WIDTH = 5
WIN_LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Player identifiers
PLAYER_X = 1
PLAYER_O = 2
current_player = PLAYER_X

# Functions
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (SCREEN_WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == PLAYER_X:
                pygame.draw.line(screen, RED, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == PLAYER_O:
                pygame.draw.circle(screen, BLUE, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_winner(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    return False

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED if player == PLAYER_X else BLUE
    pygame.draw.line(screen, color, (15, posY), (SCREEN_WIDTH - 15, posY), WIN_LINE_WIDTH)

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED if player == PLAYER_X else BLUE
    pygame.draw.line(screen, color, (posX, 15), (posX, SCREEN_HEIGHT - 15), WIN_LINE_WIDTH)

def draw_asc_diagonal(player):
    color = RED if player == PLAYER_X else BLUE
    pygame.draw.line(screen, color, (15, SCREEN_HEIGHT - 15), (SCREEN_WIDTH - 15, 15), WIN_LINE_WIDTH)

def draw_desc_diagonal(player):
    color = RED if player == PLAYER_X else BLUE
    pygame.draw.line(screen, color, (15, 15), (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15), WIN_LINE_WIDTH)

def restart():
    global board, current_player
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    current_player = PLAYER_X
    screen.fill(WHITE)
    draw_lines()

# Game loop
screen.fill(WHITE)
draw_lines()
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # X coordinate
            mouseY = event.pos[1]  # Y coordinate

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, current_player)
                if check_winner(current_player):
                    game_over = True
                current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()