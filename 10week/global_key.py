# 전역변수 정의
a = 100  # 전역변수 a는 프로그램 전체에서 접근할 수 있는 변수

def my_func():
    # 전역변수 a를 함수 내에서 수정할 수 있도록 선언
    global a
    a = 30  # 전역변수 a의 값을 30으로 변경
    # 함수 내에서 변경된 전역변수 a의 값을 출력
    print(f'my_func : {a}')

# my_func 함수 호출
# 이 호출로 인해 전역변수 a의 값이 30으로 변경됨
my_func()

# 함수 호출 후, 전역변수 a의 값을 출력
# 변경된 값인 30이 출력됨
print(a)