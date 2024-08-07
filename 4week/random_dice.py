import random  # random 모듈을 사용하여 난수를 생성합니다.

roll_count = 0  # 주사위를 던진 횟수를 기록하는 변수

while True:
    # 1부터 13까지의 난수를 4개의 주사위 숫자로 생성합니다.
    d1 = random.randint(1, 13)
    d2 = random.randint(1, 13)
    d3 = random.randint(1, 13)
    d4 = random.randint(1, 13)

    # 주사위를 던진 횟수를 증가시킵니다.
    roll_count += 1

    # 4개의 주사위 숫자가 모두 같은지 확인합니다.
    if d1 == d2 and d2 == d3 and d3 == d4:
        # 모두 같으면 결과를 출력합니다.
        print(f'주사위의 숫자 : {d1}')
        print(f'주사위를 던진 횟수 : {roll_count}')
        break  # 동일한 숫자가 나왔으므로 루프를 종료합니다.
