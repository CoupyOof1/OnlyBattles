import pygame
import sys
import random
import math
from data import * # Imports all the variables and functions in this file onto the current opened one
from events import * 

# Initialize Pygame
pygame.init()
pygame.display.set_caption('OnlyBattles'+UPDATE_LOG) # Display Game Name on Window

#set framerate of the game
clock = pygame.time.Clock()
FPS = 60 

def main_loop():
    while True: 
        clock.tick(FPS)
        updating_screens()
        pygame.display.update()

# Runs the main loop functionto continously run the game on loop
if __name__ == "__main__":
    main_loop()