import random

roll_count = 0
while True:
    d1 = random.randint(1,13)
    d2 = random.randint(1,13)
    d3 = random.randint(1,13)
    d4 = random.randint(1,13)
    roll_count += 1
    if d1 == d2 and d2 == d3 and d3 == d4:
        print(f'주사위의 숫자 : {d1}')
        print(f'주사위를 던진 횟수 : {roll_count}')
        break