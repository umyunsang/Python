a = 100

def my_func():  # 전역변수 a를 30으로 변경하는 코드
    global a
    a = 30  # 전역변수 a를 30으로 변경
    print(f'my_func : {a}')


my_func()
print(a)