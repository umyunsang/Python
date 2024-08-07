# 지뢰찾기 게임의 그리드 (격자) 초기화
grid = [
    ['-', '*', '-', '-', '-'],  # [0] 행
    ['-', '-', '-', '*', '-'],  # [1] 행
    ['-', '*', '-', '-', '-'],  # [2] 행
    ['-', '-', '-', '-', '-']   # [3] 행
]

# 결과를 저장할 리스트 초기화
result = []

# result 리스트를 grid와 같은 크기로 초기화
for _ in range(len(grid)):
    result += [[0] * len(grid[0])]

# 지뢰 주변 숫자 계산
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '*':  # 현재 위치가 지뢰가 아닌 경우
            count = 0
            # 현재 위치를 중심으로 3x3 범위를 검사
            for a in range(i - 1, i + 2):
                for b in range(j - 1, j + 2):
                    # 그리드의 범위를 벗어나지 않도록 검사
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                        if grid[a][b] == '*':  # 지뢰가 있으면 count 증가
                            count += 1
            result[i][j] = count  # 현재 위치에 주변 지뢰 개수 기록
        else:
            result[i][j] = '*'  # 지뢰인 경우, 결과에도 지뢰로 표시

# 결과 출력
for x in result:
    print(x)
