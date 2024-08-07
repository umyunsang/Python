# 초기값 설정
hap, i, mul = 3, 1, 1

# 최대 반복 횟수를 설정하여 무한 루프를 방지합니다.
max_iterations = 1000
count = 0

while count < max_iterations:
    # 현재 i에 기반하여 분모를 계산합니다.
    mul = (i * 2) * (i * 2 + 1) * (i * 2 + 2)

    # i가 홀수일 때 hap에 4/mul을 더하고,
    # 짝수일 때 hap에서 4/mul을 뺍니다.
    if i % 2 == 1:
        hap += 4 / mul
    else:
        hap -= 4 / mul

    # 현재 hap 값을 출력합니다.
    print(hap)

    # i를 1 증가시킵니다.
    i += 1
    count += 1

# 반복이 종료된 후 최종 결과를 출력합니다.
print("계산 종료.")
