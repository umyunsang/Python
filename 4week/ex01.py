hap = 0
for i in range(1000, 2001):
    if i % 2 == 1: # i가 홀수
        hap += i
print(f'누적합 : {hap}')