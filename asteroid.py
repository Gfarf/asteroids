import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        a = random.uniform(20, 50)
        vel1 = self.velocity.rotate(a)
        vel2 = self.velocity.rotate(-a)
        nr = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, nr)
        ast1.velocity = vel1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, nr)
        ast2.velocity = vel2 * 1.2
        