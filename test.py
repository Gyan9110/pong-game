import pygame
import random

pygame.init()

# Game Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
exit_game = False

# Creating game window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Pong")
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
pygame.display.update()

# Creating paddles and the ball
player1_paddle = pygame.Rect(screen_width // 2 - 50, screen_height - 20, 100, 10)  #left or x cordinate, top or y coordinate, width, height
player2_paddle = pygame.Rect(screen_width // 2 - 50, screen_height - 580, 100, 10)
ball = pygame.Rect(screen_width // 2 - 10, screen_height // 2 - 10, 20, 20)
ball_direction = [random.choice((1, -1)), 1]
'''This part of the code uses the random.choice() to randomly select one of the two values from the tuple (1, -1).
1: This represents a direction in the positive X-axis. In a 2D game, it typically means that the ball will move to the right.
-1: This represents a direction in the negative X-axis. In a 2D game, it typically means that the ball will move to the left.
1: Second 1 for Y -direction
'''

# defining welcome screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Welcome_Page
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        text_screen("Welcome to Pong Game!!", white, 220, 260)
        text_screen('Press "SPACE" to continue', white, 200, 300)
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

# Winning page
# def winner(text):
#     gameWindow.fill(black)
#     text_screen(f"The winner is : {text}", green, 220, 260)
#     text_screen('Press "Enter" to continue', white, 200, 300)
#     pygame.display.update()
#     clock.tick(60)

# Game Loop
def gameLoop():

    # Game specific variables
    exit_game = False
    game_over = False
    ball_speed = 5
    paddle_speed = 10
    fps = 60

    while not exit_game:
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player1_paddle.left > 0:
                player1_paddle.move_ip(-paddle_speed, 0)
            if keys[pygame.K_RIGHT] and player1_paddle.right < screen_width:
                player1_paddle.move_ip(paddle_speed, 0)
            if keys[pygame.K_a] and player2_paddle.left > 0:
                player2_paddle.move_ip(-paddle_speed, 0)
            if keys[pygame.K_d] and player2_paddle.right < screen_width:
                player2_paddle.move_ip(paddle_speed, 0)

            # ball movement
            ball.move_ip(ball_direction[0] * ball_speed, ball_direction[1] * ball_speed)

            # ball collision with the wall
            if ball.left == 0 or ball.right == screen_width:
                ball_direction[0] *= -1

            # ball out of bound condition or game over condition
            if ball.bottom >= screen_height:
                # winner("Player 1")
                game_over = True
            if ball.top <= 0:
                # winner("Player 2")
                game_over = True

            # ball collision with the paddle
            if ball.colliderect(player1_paddle) and ball_direction[1] == 1:
                ball_direction[1] *= -1
            if ball.colliderect(player2_paddle) and ball_direction[1] == -1:
                ball_direction[1] *= -1

            # Clearing the screen
            gameWindow.fill(black)

            # Drawing paddles and the ball
            pygame.draw.rect(gameWindow, white, player1_paddle)
            pygame.draw.rect(gameWindow, white, player2_paddle)
            pygame.draw.ellipse(gameWindow, white, ball)

        # update the display
        pygame.display.update()

        # capture the fps
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
