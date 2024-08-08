# 짝수일 때 : / 2
# 홀수일 때 : * 3 + 1
# 1이 될 때까지 몇 번 수행해야 하는가?
# 500을 넘어서면 -1을 반환

def solution(n):
    # 수행 횟수를 세기 위한 변수 초기화
    step_count = 0

    # n이 1이 될 때까지 반복
    while n != 1:
        # 수행 횟수가 500을 초과하면 -1을 반환
        if step_count == 500:
            step_count = -1
            break

        # 수행 횟수 증가
        step_count += 1

        # n이 짝수일 때
        if n % 2 == 0:
            n = n / 2
        # n이 홀수일 때
        else:
            n = n * 3 + 1

    return step_count

# 테스트 케이스
arr = [6, 16, 626331]
for a in arr:
    print(solution(a))
