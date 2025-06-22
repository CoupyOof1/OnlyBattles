import pygame 

# Initialize Pygame
pygame.init()

# Change for each update made (Michael I know you are reading this)
UPDATE_LOG = '0.0.2'

OB_EVENTS = "MENU" # An variable holding the game current events being show to the player

# Screen dimensions
WIDTH, HEIGHT = 1200, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#region All Colours 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)  # Color for running
ORANGE = (255, 151, 23)
#endregion

#region Functions 
def draw_text(text, x, y, size, color, FONT=None):
    font = pygame.font.Font(FONT, size)  # Load the font with the specified size
    text_surface = font.render(text, True, color)  # Render the text surface with the specified color
    text_rect = text_surface.get_rect(center=(x, y))  # Position the text at the given (x, y) coordinates
    screen.blit(text_surface, text_rect)  # Draw the text on the screen'''
#endregion 