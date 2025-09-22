# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    # pygame init
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Assign groups to classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    # Create a new GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    # create loop
    loop_flag = True
    while (loop_flag == True):
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
              return
       screen.fill('black')
       time_passed = clock.tick(60)
       dt = time_passed / 1000
       updatable.update(dt)
       for drawable_group in drawable:
          drawable_group.draw(screen)
       
       for asteroid in asteroids:
           if player.collide(asteroid):
               loop_flag = False
               print("Game Over!")
 
           for shot in shots:
               if asteroid.collide(shot):
                  asteroid.split()
                  shot.kill()

       pygame.display.flip()

if __name__ == "__main__":
    main()
