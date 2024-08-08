import random

# 3개의 주사위 굴리기
dices = [random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6)]
total = 0

# 첫 번째 주사위의 값 추가
total += dices[0]

# 주사위의 점수 계산
for idx in range(2):
    # 두 번째 주사위부터 계산
    if dices[idx] == 1:
        total += 0  # 주사위 값이 1일 경우 점수 추가 없음
    elif dices[idx] == 6:
        total += dices[idx + 1] * 2  # 주사위 값이 6일 경우 다음 주사위의 값 * 2 추가
    else:
        total += dices[idx + 1]  # 그 외 경우에는 다음 주사위의 값 추가

print(f'{dices} -> {total}')
