import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("벽돌 깨기 게임")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 패들 설정
paddle_width = 100
paddle_height = 12
paddle_speed = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2,
                     screen_height - 40,
                     paddle_width, paddle_height)

# 공 설정
ball_radius = 10
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = -5
ball = pygame.Rect(screen_width // 2 - ball_radius,
                   screen_height // 2 - ball_radius,
                   ball_radius * 2, ball_radius * 2)

# 벽돌 설정
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 30
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        bricks.append((brick_rect, brick_color))

# 게임 루프
isGameOver = False
clock = pygame.time.Clock()

while not isGameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOver = True

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # 공 이동
    ball.left += ball_speed_x
    ball.top += ball_speed_y

    # 공 벽 충돌
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= screen_height:
        isGameOver = True

    # 공 패들 충돌
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # 공 벽돌 충돌
    for brick in bricks[:]:
        if ball.colliderect(brick[0]):
            ball_speed_y *= -1
            bricks.remove(brick)
            break

    # 화면 그리기
    screen.fill(black)

    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, white, ball)
    for brick in bricks:
        pygame.draw.rect(screen, brick[1], brick[0])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
