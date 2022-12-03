# import and create window
import math
import random
import time

import pygame

# name
pygame.display.set_caption("pong")
icon = pygame.image.load("window icon.png")
pygame.display.set_icon(icon)

# init
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))

# score
ai_score = 0
plr_score = 0

# text

font = pygame.font.SysFont("monospace", 50)
txt = font.render("balls", 1, (255, 255, 255))


def text_ren1(text):
    score1 = font.render(text, 1, (255, 255, 255))
    screen.blit(score1, (740, 50))


def text_ren2(text):
    score2 = font.render(text, 1, (255, 255, 255))
    screen.blit(score2, (10, 50))


def win_text(text):
    wintxt = font.render(text, 1, (70, 55, 125))
    screen.blit(wintxt, (150, 150))


# ball
ball_img = pygame.image.load("ball.png")
ballX = 350
ballY = 275
ball_speed, ball_speedX = random.randint(1, 3), random.randint(1, 3)
ball_rect = ball_img.get_rect()


def checker(var1, var2):
    if var1 == 0:
        var1 = 1
        return var1
    elif var2 == 0:
        var2 = 1
        return var2


checker(ball_speed, ball_speedX)


def ball(x, y):
    screen.blit(ball_img, (x, y))


# Player 1
plr1_img = pygame.image.load("player sprite.png")
player1X = -85
player1Y = 200
player1_speed = 0
player1_rect = plr1_img.get_rect()


def player1(x, y):
    screen.blit(plr1_img, (x, y))


# Player 2 (ai)


plr2_img = pygame.image.load("player sprite.png")
player2X = 660
player2Y = 200
player2_speed = 0
player2_rect = plr2_img.get_rect()


def player2(x, y):
    screen.blit(plr2_img, (x, y))


# game loop


running = True

while running:
    # RGB screen color
    screen.fill((44, 44, 44))
    # checking for when X pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player1_speed = -2

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player1_speed = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                player1_speed = 0

    # adding boundaries
    if player1Y < -5:
        player1Y = -5
    elif player1Y > 385:
        player1Y = 385

    player2Y = ballY - 75

    if player2Y > 385:
        player2Y = 385
    elif player2Y < -5:
        player2Y = -5

    # wall boundaries
    if ballY < -10:
        ballY = -10
        ball_speed *= -1
    elif ballY > 570:
        ballY = 570
        ball_speed *= -1
        ball_speedX *= 1
    # side boundaries (reset game if touched)
    elif ballX >= 760:
        plr_score += 1
        ballX = 350
        ballY = 275
        ball_speed = random.randint(1, 3)
        ball_speedX = random.randint(1, 3)
        checker(ball_speed, ball_speedX)
        time.sleep(0.3)
    elif ballX <= -10:
        ai_score += 1
        ballX = 350
        ballY = 275
        ball_speed = random.randint(1, 3)
        ball_speedX = random.randint(1, 3)
        checker(ball_speed, ball_speedX)
        time.sleep(0.3)
    # another if statement for players cause other one is long and ugly
    if math.floor(player2X - ballX) <= -60:
        ball_speed *= 1
        ball_speedX *= -1
    elif math.floor(player1X - ballX) >= -95 and math.floor(player1Y - ballY) < 0 and math.floor(
            player1Y - ballY) > -200:
        ball_speed *= 1
        ball_speedX *= -1

    # end screen
    if ai_score == 5:
        win_text("unbeatable ai won")
        pygame.display.update()
        time.sleep(3)
        ai_score = 0
        plr_score = 0

    # updating items

    player1Y += player1_speed
    ballY += ball_speed
    ballX += ball_speedX
    player1(player1X, player1Y)
    player2(player2X, player2Y)
    ball(ballX, ballY)
    text_ren1(str(ai_score))
    text_ren2(str(plr_score))
    # updating screen
    pygame.display.update()
