# for 루프와 continue 문을 사용한 예제

# 0부터 2까지의 정수 범위에서 반복
for i in range(3):
    # i와 1을 출력합니다.
    print(i, 1)
    # i와 2를 출력합니다.
    print(i, 2)

    # continue 문을 만나면, 이후 코드 블록을 건너뛰고 루프의 다음 반복으로 이동합니다.
    continue

    # continue 이후의 코드는 실행되지 않습니다.
    # i와 3을 출력합니다. (실행되지 않음)
    print(i, 3)
    # i와 4를 출력합니다. (실행되지 않음)

# continue를 활용하여 짝수만 출력하는 예제
for i in range(5):
    if i % 2 != 0:  # i가 홀수일 경우
        continue  # 홀수는 건너뛰고, 다음 반복으로 이동
    print(i)  # 짝수만 출력
