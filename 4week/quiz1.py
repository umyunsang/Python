hap, i, mul = 3, 1, 1
while True:
    mul = (i * 2) * (i * 2 + 1) * (i * 2 + 2)
    if i % 2 == 1:
        hap += 4/mul
    else:
        hap -= 4/mul
    print(hap)
    i += 1


# 3 + 4/(2*3*4)-4/(4*5*6) ...

# n = 2
# result = 3
# sign = 1
# while True:
#     mul = 1
#     for i in range(n, n+3):
#         print(i, end=' ')
#         mul = mul * i
#     print(f'누적곱 : {mul}')
#     result = result + sign * 4 /mul
#     print(f'결과 : {result}')
#     n += 2
#     sign = -sign
