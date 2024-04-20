import random
dices = [random.randint(1,6),
         random.randint(1,6),
         random.randint(1,6)]
total = 0

# 0번 인덱스 주사위
total += dices[0]

for idx in range(2):

# 1번 인덱스 주사위
    if dices[idx] == 1:
        total += 0
    elif dices[idx] == 6:
        total += dices[idx+1] * 2
    else:
        total += dices[idx+1]

print(f'{dices} -> {total}')