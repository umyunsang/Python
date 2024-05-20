# 주어진 리스트에서 0부터 9 사이의 숫자 중 없는 숫자의 총합

def solution(nums):
    # result = 0
    # for n in range(10): # 0부터 9까지...
    #     if n not in nums:
    #         result += n

    # 최대값 - 있는 숫자의 합 = 없는 숫자의 합
    result = sum(range(10)) - sum(nums)
    return result



numbers = [[1, 2, 3, 4, 6, 7, 8, 0], [5, 8, 4, 0, 6, 7, 9]]
for n in numbers:
    print(solution(n))