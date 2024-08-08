def solution(a, b):
    """
    두 벡터 a와 b의 내적을 계산합니다. 내적(Inner product)은 벡터의 각 위치의 요소들을 곱한 후, 그 결과를 모두 더한 값입니다.
    이 연산은 머신러닝 및 딥러닝 분야에서 매우 중요한 연산입니다.

    Parameters:
    a (list of int): 첫 번째 벡터
    b (list of int): 두 번째 벡터

    Returns:
    int: 두 벡터의 내적 값
    """

    # (1) 내적을 계산하는 방법: for문을 사용한 방식
    # result = 0
    # for idx in range(len(a)):
    #     result += a[idx] * b[idx]

    # (2) 내적을 계산하는 방법: List comprehension과 sum() 함수를 사용한 방식
    result = sum([a[idx] * b[idx] for idx in range(len(a))])

    return result


# 테스트 케이스 1
a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]
print(solution(a, b))  # 예상 결과: 1*(-3) + 2*(-1) + 3*0 + 4*2 = -3 - 2 + 0 + 8 = 3

# 테스트 케이스 2
a = [-1, 0, 1]
b = [1, 0, -1]
print(solution(a, b))  # 예상 결과: -1*1 + 0*0 + 1*(-1) = -1 + 0 - 1 = -2
