# PyGame Arcade Game Project by Eevee

# Import the PyGame libraries
import pygame
import sys

# Initialize PyGame's internal variables
pygame.init()

# Set up variables for the screen size in pixels
screen_width = 640
screen_height = 480

# Initialize a window with the screen size you set
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
bg_color = (45, 76, 180)  # Blue

# ==========================
# ===== MAIN GAME LOOP =====
# ==========================
while True:
    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when you close the game window
        if event.type == pygame.QUIT:
            sys.exit()

    # Fill the screen with a solid color
    screen.fill(bg_color)

    # At the end of each game loop, call pygame.display.flip() to update the screen with all of your sprites
    pygame.display.flip()