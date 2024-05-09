a = 100

def my_func():
    b = 50
    def my_func2():
        return a + b
    print(a,b)
    print(my_func2())

my_func()
# print(b)
