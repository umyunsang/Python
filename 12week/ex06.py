# 정수 a, b를 받아서 a부터 b까지의 숫자 합
# a와 b의 대소관계는 정해져있지 않다

def solution(a, b):
    if a > b:
        a, b = b, a

    # 삼항연산자(Tri-op)
    # 변수 = 참일 때의 값 if 조건식 else 거짓일 때의 값
    a, b = (b, a) if a > b else (a, b)
    
    hap = 0
    for i in range(a, b+1):
        hap += i

    hap = sum(list(range(a, b+1)))
    return hap

a_list = [3, 3, 5]
b_list = [5, 3, 3]

for v1, v2 in zip(a_list, b_list):
    print(solution(v1, v2))