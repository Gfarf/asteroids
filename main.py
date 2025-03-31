import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    tiros = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (tiros, drawable, updatable)

    campo_de_asteroides = AsteroidField()
    nave = Player(x=SCREEN_WIDTH /2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for ast in asteroids:
            if ast.collision(nave):
                print("Game Over!")
                return
            for bullet in tiros:
                if ast.collision(bullet):
                    bullet.kill()
                    ast.split()

        screen.fill(color="black")

        for unit in drawable:
            unit.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) /1000



if __name__ == "__main__":
    main()