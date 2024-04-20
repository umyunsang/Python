grid = [#['-']
    ['-', '*', '-', '-', '-'],  # [0] i a
    ['-', '-', '-', '*', '-'],  # [1] i a
    ['-', '*', '-', '-', '-'],  # [2] i a
    ['-', '-', '-', '-', '-']  # [3] i a
]
result = []

for _ in range(len(grid)):
    result += [[0] * len(grid[0])]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '*':
            count = 0
            for a in range(i - 1, i + 1 + 1):
                for b in range(j - 1, j + 1 + 1):
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                        if grid[a][b] == '*':
                            count += 1
            result[i][j] = count
        else:
            result[i][j] = '*'

for x in result:
    print(x)
