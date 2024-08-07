# 전역변수 정의
a = 100


def my_func():
    # my_func 내에서 사용할 지역변수 b 정의
    b = 50

    def my_func2():
        # my_func2는 my_func의 지역변수 b와 전역변수 a에 접근할 수 있음
        # my_func2 내에서 a는 전역변수, b는 my_func의 지역변수
        return a + b

    # my_func 내에서 전역변수 a와 지역변수 b의 값을 출력
    print(a, b)
    # my_func2 호출 및 반환값 출력
    print(my_func2())


# my_func 호출
# 이 호출로 인해 a와 b의 값이 출력되고, my_func2()의 반환값도 출력됨
my_func()

# 주석 처리된 코드
# print(b)  # 오류 발생: b는 my_func의 지역변수이므로 my_func 외부에서는 접근 불가
