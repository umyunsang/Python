# 함수 : 입력값(파라미터)를 전달받고,
# 전달 받은 파라미터를 이용해 지정한 처리를 수행한 후
# 그 결과를 반환

# 함수의 문법
# def 함수이름(입력1,입력2,...):
#   처리코드
#   ...
#   return 반환값

# 입력값과 반환값은 있어도 되고 없어도 됨

# 1. 입력 X, 반환 X
def my_func1():
    print('my_func1 호출')


my_func1()


# 2. 입력이 하나만 존재할 때
def my_func2(v1):  # v1 : 파라미터(parameter)
    print(f'my_func2 호출 : {v1}')


a = 100
my_func2(a)  # a : argument


# 3. 입력이 여러 개 존재할 때
def my_func3(v1, v2, v3):
    res = v1 + v2 - v3
    print(f'my_func3 : {v1} + {v2} - {v3} = {res}')


my_func3(10, 20, 5)


# 4. 반환값이 1개일 때
def my_func4(v1, v2, v3):
    res = v1 + v2 - v3
    print(f'my_func3 : {v1} + {v2} - {v3} = {res}')
    return res


r1 = my_func4(10, 20, 5)
print(f'my_func4의 결과 : {r1}')


# 5. 반환값이 여러 개일 때
def my_func5(num1, num2):
    mul = num1 * num2
    div = num1 / num2
    print(f'my_func5 : {num1}, {num2}')
    return mul, div


r1, r2 = my_func5(5, 3)
print(f'my_func5의 결과 : {r1}, {r2}')

# 모든 프로그래밍 언어에서 함수의 반환값은 하나만 가능하다
