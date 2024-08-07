# 팩토리얼을 구하는 프로그램
# 팩토리얼(n!) -> 자연수 n이 주어졌을 때 1부터 n까지의 곱을 계산한 값

# 초기값 설정
fac = 1

# 사용자로부터 자연수 N을 입력받기
N = int(input('N을 입력 ==> '))

# 결과 문자열 초기화
msg = f'{N}!은 '

# 1부터 N까지의 곱을 계산하고 결과 문자열을 생성
for n in range(1, N + 1):
    msg += f'{n}'
    fac = fac * n
    # 마지막 숫자가 아닌 경우 '*' 추가
    if n != N:
        msg += ' * '

# 결과 출력
print(f'{msg} 이므로 {fac}입니다')
