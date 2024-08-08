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
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2,  # 패들 위치 설정
                     screen_height - 40,  # 화면 하단에 위치
                     paddle_width, paddle_height)

# 공 설정
ball_radius = 10
ball_speed_x = 5 * random.choice((1, -1))  # 공의 초기 속도와 방향 랜덤 설정
ball_speed_y = -5
ball = pygame.Rect(screen_width // 2 - ball_radius,  # 공의 위치 설정
                   screen_height // 2 - ball_radius,
                   ball_radius * 2, ball_radius * 2)

# 벽돌 설정
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols  # 벽돌의 폭 계산
brick_height = 30
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width  # 벽돌의 x 좌표
        brick_y = row * brick_height  # 벽돌의 y 좌표
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)  # 벽돌의 사각형 영역
        brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 랜덤 색상
        bricks.append((brick_rect, brick_color))  # 벽돌 목록에 추가

# 게임 루프
isGameOver = False
clock = pygame.time.Clock()

while not isGameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 종료 이벤트
            isGameOver = True

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:  # 왼쪽으로 이동
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:  # 오른쪽으로 이동
        paddle.right += paddle_speed

    # 공 이동
    ball.left += ball_speed_x
    ball.top += ball_speed_y

    # 공 벽 충돌 처리
    if ball.left <= 0 or ball.right >= screen_width:  # 좌우 벽 충돌
        ball_speed_x *= -1
    if ball.top <= 0:  # 상단 벽 충돌
        ball_speed_y *= -1
    if ball.bottom >= screen_height:  # 하단 벽 충돌 (게임 오버)
        isGameOver = True

    # 공과 패들 충돌 처리
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # 공과 벽돌 충돌 처리
    for brick in bricks[:]:  # 벽돌 목록을 복사하여 순회
        if ball.colliderect(brick[0]):  # 공과 벽돌 충돌
            ball_speed_y *= -1
            bricks.remove(brick)  # 충돌한 벽돌 제거
            break

    # 화면 그리기
    screen.fill(black)  # 배경 색상 채우기

    pygame.draw.rect(screen, white, paddle)  # 패들 그리기
    pygame.draw.ellipse(screen, white, ball)  # 공 그리기
    for brick in bricks:  # 벽돌 그리기
        pygame.draw.rect(screen, brick[1], brick[0])

    pygame.display.flip()  # 화면 업데이트
    clock.tick(60)  # 초당 60 프레임

pygame.quit()
