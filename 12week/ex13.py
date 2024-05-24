# 두 행렬의 합
def solution(arr1, arr2):
    # result = []
    # y = len(arr1) # 행 길이
    # x = len(arr1[0]) # 열 길이
    # for row in range(y):
    #     result.append([0] * x)


    y = len(arr1) # 행 길이
    x = len(arr1[0]) # 열 길이
    result = arr1.copy()

    for row in range(y):
        for col in range(x):
            result[row][col] = arr1[row][col] + arr2[row][col]
    return result




arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))

arr1 = [[1],[2]]
arr2 = [[3],[4]]
print(solution(arr1, arr2))