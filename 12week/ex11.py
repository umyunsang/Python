# 정수 n, m이 주어졌을 때
# 가로 n x 세로 m 의 형태로
# 직사각형 모양의 '*'을 출력
def solution(n, m):
    for row in range(m):
        print('*' * n)

solution(5, 3)