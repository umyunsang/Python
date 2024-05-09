a = 100 # 전역변수


def my_func(a):
    b = 33
    print(f'my_func : {a, b}')


print(a)
my_func(55)
