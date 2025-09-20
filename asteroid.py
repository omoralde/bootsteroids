import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.random_angle = random.uniform(20, 50)
        self.asteroid_velocity_pos = self.velocity.rotate(self.random_angle)
        self.asteroid_velocity_neg = self.velocity.rotate(-self.random_angle)
        self.new_radius = (self.radius - ASTEROID_MIN_RADIUS)
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid_1.velocity = self.asteroid_velocity_pos * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid_2.velocity = self.asteroid_velocity_neg * 1.2

