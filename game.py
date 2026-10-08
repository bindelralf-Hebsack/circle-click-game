import random
import math


class CircleGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.radius = 28
        self.score = 0
        self.misses = 0
        self.max_misses = 3
        self.game_over = False
        self.speed = 3.0
        self.x = random.randint(self.radius, self.width - self.radius)
        self.y = random.randint(self.radius, self.height - self.radius)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        self._normalize_direction()

    def _normalize_direction(self):
        length = math.hypot(self.direction_x, self.direction_y)
        if length == 0:
            self.direction_x = 1
            self.direction_y = 0
            length = 1
        self.direction_x /= length
        self.direction_y /= length

    def update(self):
        if self.game_over:
            return

        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed

        if self.x <= self.radius or self.x >= self.width - self.radius:
            self.direction_x *= -1
            self.x = max(self.radius, min(self.x, self.width - self.radius))

        if self.y <= self.radius or self.y >= self.height - self.radius:
            self.direction_y *= -1
            self.y = max(self.radius, min(self.y, self.height - self.radius))

    def handle_click(self, mouse_pos):
        if self.game_over:
            return

        mouse_x, mouse_y = mouse_pos
        distance = math.hypot(mouse_x - self.x, mouse_y - self.y)

        if distance <= self.radius:
            self.score += 1
            self.speed = min(3 + self.score * 0.6, 16)
            self._respawn_circle()
        else:
            self.misses += 1
            if self.misses >= self.max_misses:
                self.game_over = True

    def _respawn_circle(self):
        self.x = random.randint(self.radius, self.width - self.radius)
        self.y = random.randint(self.radius, self.height - self.radius)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        self._normalize_direction()

    def is_hit(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        return math.hypot(mouse_x - self.x, mouse_y - self.y) <= self.radius
