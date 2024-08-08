# 주어진 리스트에서 0부터 9 사이의 숫자 중 없는 숫자의 총합

def solution(nums):
    # (1) 직접적인 방법
    # result = 0
    # for n in range(10):  # 0부터 9까지 숫자 확인
    #     if n not in nums:  # nums 리스트에 n이 없는 경우
    #         result += n  # result에 n을 더함

    # (2) 수학적인 방법
    # 모든 숫자의 합 - 존재하는 숫자의 합 = 없는 숫자의 합
    total_sum = sum(range(10))  # 0부터 9까지의 합: 45
    nums_sum = sum(nums)  # nums 리스트에 있는 숫자들의 합
    result = total_sum - nums_sum  # 없는 숫자의 합 계산
    return result

# 테스트 케이스
numbers = [[1, 2, 3, 4, 6, 7, 8, 0], [5, 8, 4, 0, 6, 7, 9]]

# 각 numbers 리스트에 대해 solution 함수 실행
for n in numbers:
    print(solution(n))  # 결과: 15, 15
