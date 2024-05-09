def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v1 - v2
    if op == '*':
        return v1 * v2
    if op == '/':
        return v1 / v2


op = input('연산자 (+,-,*,/) : ')
v1 = int(input('숫자 1 :'))
v2 = int(input('숫자 2 :'))
res = calc(v1,v2,op)
print(f'{v1} {op} {v2} = {res}')