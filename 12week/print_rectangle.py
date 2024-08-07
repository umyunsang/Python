# 정수 n, m이 주어졌을 때
# 가로 n x 세로 m 의 형태로
# 직사각형 모양의 '*'을 출력
def solution(n, m):
    """
    주어진 가로(n)와 세로(m) 크기에 따라 '*'로 직사각형 모양을 출력합니다.

    Parameters:
    n (int): 직사각형의 가로 길이
    m (int): 직사각형의 세로 길이
    """
    # 세로 방향으로 m만큼 반복
    for row in range(m):
        # 가로 방향으로 n만큼 '*'을 출력
        print('*' * n)


# 함수 호출 예제
solution(5, 3)  # 5x3 직사각형을 출력합니다
