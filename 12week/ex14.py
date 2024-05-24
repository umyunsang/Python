# a와 b의 내적(Inner product) -> AI분야에서 딥러닝의 핵심 연산
#                              컨벌루션(Convolution) - Convolutional Neural Networks

# 각 위치의 요소들의 곱을 합한 것
def solution(a, b):
    # result = 0
    # for idx in range(len(a)):
    #     result += a[idx] * b[idx]

    result = sum([a[idx] * b[idx] for idx in range(len(a))])
    return result





a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]
print(solution(a, b))

a = [-1, 0, 1]
b = [1, 0, -1]
print(solution(a, b))