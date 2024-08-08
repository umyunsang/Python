# 두 행렬의 합
def solution(arr1, arr2):
    # result = []
    # y = len(arr1) # 행 길이
    # x = len(arr1[0]) # 열 길이
    # for row in range(y):
    #     result.append([0] * x)

    y = len(arr1)  # 행 길이
    x = len(arr1[0])  # 열 길이
    result = arr1.copy()

    for row in range(y):
        for col in range(x):
            result[row][col] = arr1[row][col] + arr2[row][col]
    return result


# 테스트 케이스 1: 2x2 행렬
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
print(solution(arr1, arr2))  # 예상 결과: [[4, 6], [7, 9]]

# 테스트 케이스 2: 2x1 행렬
arr1 = [[1], [2]]
arr2 = [[3], [4]]
print(solution(arr1, arr2))  # 예상 결과: [[4], [6]]
