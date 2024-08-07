import random

# 사용자로부터 행렬의 크기 N을 입력받음
N = int(input("행렬의 크기 N을 입력하세요: "))

# 리스트 컴프리헨션을 이용하여 N x N 크기의 행렬을 생성
# 각 요소는 -100부터 100 사이의 무작위 정수로 초기화
list_input = [[random.randint(-100, 100) for _ in range(N)] for _ in range(N)]

# 생성된 행렬을 출력
print("생성된 행렬:")
for row in list_input:
    print(row)

# 주 대각선의 합과 부 대각선의 합을 초기화
hap_up, hap_down = 0, 0

# 주 대각선 (왼쪽 상단부터 오른쪽 하단) 의 합을 계산
for i in range(N):
    hap_up += list_input[i][i]

# 부 대각선 (왼쪽 하단부터 오른쪽 상단) 의 합을 계산
for i in range(N):
    hap_down += list_input[i][-i-1]

# 결과를 출력
print(f'주 대각선의 합 : {hap_up}')
print(f'부 대각선의 합 : {hap_down}')
