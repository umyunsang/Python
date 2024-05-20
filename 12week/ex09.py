# 주어진 리스트(absolutes)에 포함된 값에
# signs의 진리값을 부호로 적용한 값의 총합

def solution(nums, signs):
    # (1) 직접적인 총합 계산
    # result = 0
    # for idx in range(len(signs)):
    #     if signs[idx]: # signs[idx]가 True면...
    #         result += nums[idx]
    #     else:
    #         result -= nums[idx]

    # (2) 부호를 선반영
    result = [nums[idx] if signs[idx] else -nums[idx] for idx in range(len(signs))]
    result = sum(result)
    return result


absolutes = [[4, 7, 12], [1, 2, 3]]
signs = [[True, False, True], [False, False, True]]

for a, s in zip(absolutes, signs):
    print(solution(a, s))



