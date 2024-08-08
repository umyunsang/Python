# 주어진 리스트(absolutes)에 포함된 값에
# signs의 진리값을 부호로 적용한 값의 총합

def solution(nums, signs):
    # (1) 직접적인 총합 계산
    # 결과를 저장할 변수 초기화
    # result = 0
    # # 각 인덱스에 대해 부호를 반영하여 총합 계산
    # for idx in range(len(signs)):
    #     if signs[idx]:  # signs[idx]가 True이면...
    #         result += nums[idx]  # 양수 추가
    #     else:
    #         result -= nums[idx]  # 음수 추가

    # (2) 리스트 컴프리헨션을 사용하여 부호를 반영한 값 계산
    # 부호가 True인 경우 해당 값을 그대로, False인 경우 음수로 변환
    result = [nums[idx] if signs[idx] else -nums[idx] for idx in range(len(signs))]

    # 결과 리스트의 총합 계산
    result = sum(result)

    return result


# 테스트 케이스
absolutes = [[4, 7, 12], [1, 2, 3]]
signs = [[True, False, True], [False, False, True]]

# 각 absolutes와 signs 쌍에 대해 solution 함수 실행
for a, s in zip(absolutes, signs):
    print(solution(a, s))  # 결과: 9, 0
