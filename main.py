# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    # pygame init
    pygame.init()
    # Create a new GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create loop
    loop_flag = True
    while (loop_flag == True):
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
              return
       screen.fill('black')
       pygame.display.flip()

if __name__ == "__main__":
    main()
