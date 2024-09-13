import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game Variables
balance = 1000000
pill_taken = 0
deadly_pill = random.randint(1, 10)  # Random deadly pill
game_over = False

# Load Images
safe_pill_img = pygame.image.load('safe_pill.png')  # Replace with an actual image
deadly_pill_img = pygame.image.load('deadly_pill.png')  # Replace with an actual image
pill_img = pygame.transform.scale(safe_pill_img, (50, 50))  # Move this line out of the main game loop

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Function to handle game over
def game_over_screen():
    screen.fill(WHITE)
    draw_text("You took the deadly pill. Game Over!", font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(f"Final Balance: ${0}", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Main Game Loop
running = True
while running:
    screen.fill(WHITE)

    # Draw Game Info
    draw_text(f"Balance: ${balance:,}", font, BLACK, screen, SCREEN_WIDTH // 2, 30)
    draw_text(f"Pills Taken: {pill_taken}", font, BLACK, screen, SCREEN_WIDTH // 2, 60)
    
    # Draw Pill (This will change when the user clicks)
    pill_x = SCREEN_WIDTH // 2 - 25
    pill_y = SCREEN_HEIGHT // 2 - 25
    screen.blit(pill_img, (pill_x, pill_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # Check if player clicked on the pill
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pill_x < mouse_x < pill_x + 50 and pill_y < mouse_y < pill_y + 50:
                pill_taken += 1
                if pill_taken == deadly_pill:
                    pill_img = deadly_pill_img  # Change image to deadly pill when it's picked
                    game_over_screen()
                else:
                    balance *= 2
                    # Only update the image to safe pill once when needed, do not overwrite it every frame.

    # Update display
    pygame.display.update()
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()