import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2


  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Player.containers = (updatable, drawable)

  Asteroid.containers = (asteroids, updatable, drawable)

  AsteroidField.containers = (updatable)

  asteroid_field = AsteroidField()

  player = Player(x, y, PLAYER_RADIUS)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    for sprite in updatable:
      sprite.update(dt)

    screen.fill((0, 0, 0))
    
    for sprite in drawable:
      sprite.draw(screen)

    pygame.display.flip()
    t = clock.tick(60)
    dt = t / 1000

if __name__ == "__main__":
  main()
