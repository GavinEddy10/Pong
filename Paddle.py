from random import randint

import pygame.draw


class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 200
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.score = 0

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y


class Ball:

    def __init__(self):
        self.x = 640
        self.y = 360
        self.width = 15
        self.height = 15
        self.color = (255, 255, 255)
        self.velocity = [randint(4, 8), randint(-8, 8)]

    # handles change in velocty as well
    def check_bounce_wall(self):
        if self.x <= 0 or self.x >= 1280:
            self.velocity[0] = -self.velocity[0]
        if self.y <= 0 or self.y >= 720:
            self.velocity[1] = -self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# includes paddle for opponent
class Paddle_AI:

    def __init__(self):
        self.Paddle = Paddle(0, 0)
        self.score = 0
        self.x = 0
        self.y = 0
        self.height = self.width = 20
        self.height = 200
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def follow_ball(self, ball):
        self.y = ball.y - self.height / 2
