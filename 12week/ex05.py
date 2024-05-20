# 짝수일 때 : / 2
# 홀수일 때 : * 3 + 1
# 1이 될 때까지 몇 번 수행해야 하는가?
# 500을 넘어서면 -1을 반환

def solution(n):
    step_count = 0

    while n != 1:
        if step_count == 500:
            step_count = -1
            break

        step_count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    return step_count




arr = [6, 16, 626331]
for a in arr:
    print(solution(a))