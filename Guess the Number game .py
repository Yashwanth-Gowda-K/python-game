import pygame
import random
import sys

# Initialize pygame and set up colors
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number Game")

# Set up fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Initialize game variables
target_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
input_text = ''
message = "Guess a number between 1 and 100"
score = 0  # Initialize score
game_over = False  # Add a game over flag to control input after game ends

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and not game_over:  # Check input only if game is not over
            if event.key == pygame.K_RETURN:  # Enter key
                try:
                    guess = int(input_text)
                    attempts += 1
                    if guess < target_number:
                        message = "Too low! Try again."
                    elif guess > target_number:
                        message = "Too high! Try again."
                    else:
                        score = max(100 - (attempts - 1) * 10, 0)
                        message = f"Correct! You guessed it in {attempts} tries. Score: {score}"
                        game_over = True  # Set game over to True after correct guess
                except ValueError:
                    message = "Please enter a valid number."
                input_text = ''  # Clear input after each guess
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Check if max attempts are reached and set game over condition
    if attempts >= max_attempts and not game_over:
        message = f"Out of tries! The number was {target_number}."
        game_over = True  # Set game over to True if max attempts reached
    
    # Draw everything on the screen
    instruction = font.render("Guess the Number", True, BLACK)
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, 30))

    attempt_info = small_font.render(f"Attempt {attempts}/{max_attempts}", True, BLACK)
    screen.blit(attempt_info, (WIDTH // 2 - attempt_info.get_width() // 2, 80))

    input_display = font.render(input_text, True, BLACK)
    screen.blit(input_display, (WIDTH // 2 - input_display.get_width() // 2, 150))

    message_display = small_font.render(message, True, BLACK)
    screen.blit(message_display, (WIDTH // 2 - message_display.get_width() // 2, 250))

    pygame.display.flip()  # Update the display

# Exit pygame
pygame.quit()
