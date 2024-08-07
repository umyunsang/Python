# 종속코드는 들여쓰기로 표현

# 조건문 없이 단순히 1부터 9까지 출력
print('1')
print('2')
print('3')
print('4')
print('5')
print('6')
print('7')
print('8')
print('9')

# 조건문을 이용한 종속 코드 예제
num = 10

if num > 5:  # 조건이 참일 때 실행되는 종속 코드
    print(f'{num}은 5보다 큽니다')
    print(f'{num}은 5보다 큰 조건에 종속된 코드입니다')

print('조건문과 관련 없는 코드')  # 조건문과 관련 없는 코드

# 반복문을 이용한 종속 코드 예제
for i in range(1, 4):
    print(f'반복문 종속 코드: {i}')  # 반복문에 종속된 코드
    print(f'이 코드는 반복문에 종속되어 {i}를 출력합니다')

print('반복문과 관련 없는 코드')  # 반복문과 관련 없는 코드
