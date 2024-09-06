import pygame
from constants import *
from player import Player

def main():
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2

  player = Player(x, y, PLAYER_RADIUS)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()
    t = clock.tick(60)
    dt = t / 1000

if __name__ == "__main__":
  main()
