import pygame
import time

# Initialize pygame
pygame.init()

# Set up display
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Countdown Timer')

# Set up fonts
font = pygame.font.SysFont('Arial', 48)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Timer function
def countdown_timer(seconds):
    start_time = time.time()  # Get the starting time
    while seconds > 0:
        screen.fill(WHITE)  # Clear the screen

        # Calculate remaining time
        elapsed_time = time.time() - start_time
        remaining_time = max(0, seconds - int(elapsed_time))  # Prevent negative time
        
        # Display remaining time
        timer_text = font.render(f"{remaining_time}s", True, BLACK)
        screen.blit(timer_text, (screen_width // 2 - timer_text.get_width() // 2, screen_height // 2 - timer_text.get_height() // 2))
        
        pygame.display.update()  # Update the display

        # Check for quit event (close the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.time.delay(100)  # Delay to slow down the loop

    # Display "Time's up!" message
    screen.fill(WHITE)
    times_up_text = font.render("Time's up!", True, BLACK)
    screen.blit(times_up_text, (screen_width // 2 - times_up_text.get_width() // 2, screen_height // 2 - times_up_text.get_height() // 2))
    pygame.display.update()

    pygame.time.delay(2000)  # Show "Time's up!" for 2 seconds before closing

# Main function
def main():
    running = True
    while running:
        screen.fill(WHITE)
        display_text = font.render("Enter Time in Seconds:", True, BLACK)
        screen.blit(display_text, (screen_width // 2 - display_text.get_width() // 2, 50))

        # Input box for user to enter seconds
        input_box = pygame.Rect(screen_width // 2 - 50, 150, 100, 50)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        pygame.display.update()

        input_seconds = ""
        getting_input = True
        while getting_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # On pressing Enter
                        if input_seconds.isdigit():
                            countdown_timer(int(input_seconds))  # Start the countdown timer
                        getting_input = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_seconds = input_seconds[:-1]
                    else:
                        input_seconds += event.unicode  # Append the typed character

            # Display the input seconds
            screen.fill(WHITE)
            screen.blit(display_text, (screen_width // 2 - display_text.get_width() // 2, 50))
            text_surface = font.render(input_seconds, True, BLACK)
            screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

            pygame.display.update()
            pygame.time.delay(100)  # Delay to reduce CPU usage

# Run the main function
main()

# Quit pygame
pygame.quit()
