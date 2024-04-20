# 팩토리얼을 구하는 프로그램
# 팩토리얼 -> 자연수 n이 주어졌을 때 1부터 n까지의 곲

fac = 1
N = int(input('N을 입력 ==> '))
msg = f'{N}!은 '
for n in range(1, N+1):
    msg += f'{n}'
    fac = fac * n
    if n != N:
        msg += ' * '
print(f'{msg} 이므로 {fac}입니다')

# print(f'{N}!은 ',end=' ')
# for i in range(1, N+1):
#