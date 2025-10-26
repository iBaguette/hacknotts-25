import pygame
from random import randint, uniform


class BloodParticle:
    def __init__(self, position: tuple[int, int]):
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(uniform(-1.8, 1.8), uniform(-4.5, -1.5))
        self.size = randint(2, 4)
        self.lifetime = randint(18, 32)

    def update(self) -> None:
        self.velocity.y += 0.25
        self.position += self.velocity
        self.lifetime -= 1

    def draw(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(0, 0, self.size, self.size)
        rect.center = (int(self.position.x), int(self.position.y))
        pygame.draw.rect(surface, (140, 0, 0), rect)

    def is_alive(self, bounds: pygame.Rect) -> bool:
        return self.lifetime > 0 and bounds.collidepoint(self.position)


class BloodSystem:
    def __init__(self):
        self.particles: list[BloodParticle] = []

    def spawn(self, position: tuple[int, int], count: int = 14) -> None:
        for _ in range(count):
            self.particles.append(BloodParticle(position))

    def reset(self) -> None:
        self.particles.clear()

    def update(self, surface: pygame.Surface) -> None:
        bounds = surface.get_rect()
        survivors: list[BloodParticle] = []
        for particle in self.particles:
            particle.update()
            if particle.is_alive(bounds):
                particle.draw(surface)
                survivors.append(particle)
        self.particles = survivors