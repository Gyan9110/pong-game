import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create the paddles and ball
player_paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_direction = [random.choice((1, -1)), 1]

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_paddle.left > 0:
        player_paddle.move_ip(-PADDLE_SPEED, 0)
    if keys[pygame.K_RIGHT] and player_paddle.right < WIDTH:
        player_paddle.move_ip(PADDLE_SPEED, 0)

    # Move the ball
    ball.move_ip(ball_direction[0] * BALL_SPEED, ball_direction[1] * BALL_SPEED)

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_direction[0] *= -1
    if ball.top <= 0:
        ball_direction[1] *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) and ball_direction[1] == 1:
        ball_direction[1] *= -1

    # Ball out of bounds
    if ball.bottom >= HEIGHT:
        # Game over logic
        running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()

