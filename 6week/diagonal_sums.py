# N x N 크기의 정사각형 행렬의 주대각선과 부대각선의 합을 구하는 코드

# 행렬 리스트 (N x N)
list_input = [
    [11, -2, 4],
    [4, 5, 6],
    [10, -12, 9]
]

# 주대각선의 합 (왼쪽 상단에서 오른쪽 하단으로)
hap_up = 0
# 부대각선의 합 (왼쪽 하단에서 오른쪽 상단으로)
hap_down = 0

# 행렬의 크기 (행 또는 열의 수)
n = len(list_input)

# 주대각선의 합 계산
for i in range(n):
    hap_up += list_input[i][i]  # (i, i) 위치의 요소를 합산

# 부대각선의 합 계산
for i in range(n):
    hap_down += list_input[i][n - i - 1]  # (i, n-i-1) 위치의 요소를 합산

# 결과 출력
print(f'주대각선의 합 : {hap_up}')
print(f'부대각선의 합 : {hap_down}')
