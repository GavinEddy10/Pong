import random
import pygame

# start the pygame engine
from Paddle import *
from Game import *

pygame.init()

# start the pygame font engine
pygame.font.init()
WHITE = (255, 255, 255)
myfontTitle = pygame.font.SysFont('gabriola', 80)  # load a font for use
gameOverTitle = pygame.font.SysFont('gabriola', 80)

# Initalize Text for Title
text = myfontTitle.render('PONG', True, WHITE)
textRect = text.get_rect()
textRect.center = (642.5, 75)
display_surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('PONG')

# Initalize Text for GameOver
text4 = gameOverTitle.render('GAME OVER', True, WHITE)
textRect4 = text.get_rect()
textRect4.center = (545, 360)

# start the sound engine
pygame.mixer.init()

# game variables
simOver = False
userGame = Game()

# game independent variables (needed for every pygame)
FPS = 60  # 60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock()  # used to lock the game to 60 FPS
screen = pygame.display.set_mode((1280, 720))  # initialize the game window


def clear_screen():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280, 720))


# main while loop
while not simOver:
    # loop through and empty the event queue, key presses
    # buttons, clicks, etc.
    for event in pygame.event.get():
        # if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            simOver = True

    # draw code
    clear_screen()

    # Draw Title
    display_surface.blit(text, textRect)

    # draw userPaddle score
    UserScore = myfontTitle.render(str(userGame.userPaddle.score), True, WHITE)
    textRect2 = text.get_rect()
    textRect2.center = (900, 75)
    display_surface.blit(UserScore, textRect2)

    # draw ai Paddle Score
    AIScore = myfontTitle.render(str(userGame.AIPaddle.score), True, WHITE)
    textRect3 = text.get_rect()
    textRect3.center = (500, 75)
    display_surface.blit(AIScore, textRect3)

    if not userGame.gameOver():  # gameOver
        userGame.act(screen)
    else:
        display_surface.blit(text4, textRect4)  # final game  over screen

    pygame.draw.line(screen, (255, 255, 255), (640, 0), (640, 720), 1)
    # draw score and PONG

    # player update code

    # put all the graphics on the screen
    # should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS)  # slow the loop down to 60 loops per second
