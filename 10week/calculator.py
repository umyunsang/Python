# calc 함수 정의
# v1, v2: 두 숫자
# op: 연산자 (+, -, *, /)
# 이 함수는 연산자에 따라 v1과 v2를 연산하여 결과를 반환합니다.
def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        # 나눗셈의 경우, 0으로 나누는 것을 방지
        if v2 == 0:
            return "Error: Division by zero"
        return v1 / v2
    else:
        return "Error: Invalid operator"

# 사용자로부터 연산자와 두 숫자를 입력받음
op = input('연산자 (+, -, *, /) : ')
v1 = int(input('숫자 1 :'))
v2 = int(input('숫자 2 :'))

# calc 함수 호출하여 연산 결과를 계산
res = calc(v1, v2, op)

# 결과 출력
print(f'{v1} {op} {v2} = {res}')
