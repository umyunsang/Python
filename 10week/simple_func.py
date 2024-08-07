# 함수 정의
def my_func(a):
    # 만약 입력값 a가 0이라면, 함수는 아무것도 반환하지 않고 종료
    if a == 0:
        return

    # a에 50을 더한 값을 res에 저장
    res = a + 50

    # res의 값을 출력
    print(res)

    # res 값을 반환
    return res


# 함수 호출 예제
my_func(50)  # 입력값 50에 50을 더해 100을 출력하고 반환
