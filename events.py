import pygame 
from data import * # Imports all the variables and functions in this file onto the current opened one

# Initialize Pygame
pygame.init()

#region Updating Screens Functions 
def updating_screens():
    global OB_EVENTS # If Variables are constantly changing throughout the program we will also retrieve that new value 

    if OB_EVENTS == "MENU":
        drawing_menu()
#endregion 

#region Drawing Menu
def drawing_menu():
    draw_text("Only Battles", 600, 105, 105, WHITE, "Fonts/JMH CTH ARCADE.ttf")
#endregion

#region Drawing Team Menu 
def drawing_team_menu():
    pass
#endregion