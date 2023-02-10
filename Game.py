import pygame
from Paddle import *


class Game:

    def __init__(self):
        self.userPaddle = Paddle(1260, 360)
        self.AIPaddle = Paddle_AI()
        self.gameBall = Ball()

    def act(self, screen):
        # draw items
        self.userPaddle.draw(screen)
        self.AIPaddle.draw(screen)
        self.gameBall.draw(screen)

        # handle input
        self.AIPaddle.follow_ball(self.gameBall)
        self.handle_key_presses()

        # check if ball hits right or left wall
        self.gameBall.check_bounce_wall()
        self.gameBall.update()

        # check collision
        self.collide_detect()

    def collide_detect(self):
        g_b_rect = pygame.Rect(self.gameBall.x, self.gameBall.y, self.gameBall.width, self.gameBall.height)
        u_p_rect = pygame.Rect(self.userPaddle.x, self.userPaddle.y, self.userPaddle.width, self.userPaddle.height)
        AI_p_rect = pygame.Rect(self.AIPaddle.x, self.AIPaddle.y, self.AIPaddle.width, self.AIPaddle.height)
        if u_p_rect.colliderect(g_b_rect):
            self.userPaddle.set_score(self.userPaddle.get_score() + 1)
            self.gameBall.bounce()
        elif AI_p_rect.colliderect(g_b_rect):
            self.AIPaddle.score += 1
            self.gameBall.bounce()

    # add to computer move for AIPaddle
    def paddle_out_of_bounds(self):
        if self.AIPaddle.y < 0:
            self.AIPaddle.y = 0
        elif self.AIPaddle.y + self.AIPaddle.height > 720:
            self.AIPaddle.y = 720 - self.userPaddle.height

        if self.userPaddle.y < 0:  # past top of screen
            self.userPaddle.y = 0
        elif self.userPaddle.y + self.userPaddle.height > 720:  # past bottom of screen
            self.userPaddle.y = 720 - self.userPaddle.height

    def handle_key_presses(self):
        if pygame.key.get_pressed()[pygame.K_w]:
            self.userPaddle.set_y(self.userPaddle.get_y() - 20)
        if pygame.key.get_pressed()[pygame.K_s]:
            self.userPaddle.set_y(self.userPaddle.get_y() + 20)
        self.paddle_out_of_bounds()

    def gameOver(self):
        if self.gameBall.x >= 1280 or self.gameBall.x <= 0:
            return True
