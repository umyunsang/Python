import random

N = int(input("행렬의 크기 N을 입력하세요: "))

# 리스트 생성 및 무작위 값 채우기
list_input = [[random.randint(-100, 100) for _ in range(N)] for _ in range(N)]

# 행렬 출력
print("생성된 행렬:")
for row in list_input:
    print(row)

# 주 대각선의 합과 부 대각선의 합 초기화
hap_up, hap_down = 0, 0

# 주 대각선의 합 계산
for i in range(N):
    hap_up += list_input[i][i]

# 부 대각선의 합 계산
for i in range(N):
    hap_down += list_input[i][-i-1]

# 결과 출력
print(f'주 대각선의 합 : {hap_up}')
print(f'부 대각선의 합 : {hap_down}')
