# 파라미터에 대하여...


# 파라미터에는 기본값(default)을 지정할 수 있음
# 기본값 => 전달받은 argument가 없을 때 대신 사용되는 값
def hap_func1(v1, v2=5):
    hap = v1 + v2
    print(f'{hap}')


def hap_func2(v1, v2, v3=0, v4=0, v5=0):
    hap = v1 + v2 + v3 + v4 + v5
    print(f'{hap}')


# 입력해야 하는 정보가 많은 경우...
# 1. 리스트 또는 튜플 활용
def hap_func3(nums):
    hap = sum(nums)
    print(f'hap_func3 : {hap}')


hap_func3([1, 2, 3, 5, 3, 2])


# 2. 가변 길이 파라미터
def hap_func4(*nums):
    print(nums)
    print(type(nums))
    hap = sum(nums)
    print(f'hap_func4 : {hap}')


hap_func4(4, 9, 12)


# 가변 길이 파라미터는 항상 제일 마지막에!!
def hap_func5(v1, v2, *nums1):
    hap1 = sum(nums1)
    print(f'hap_func5 : {hap1}')


hap_func5(1, 2, 3, 4, 5, 6, 7)


# 기본값이 지정된 파라미터는 지정되지 않은 파라미터보다 뒤에 와야한다.
def hap_func6(v1, v3, v2=5):
    hap = v1 + v2 + v3


hap_func6(2, 5)
hap_func6(v1=2, v2=6, v3=11)    # argument가 어떤 파라미터에 대입되어야 하는지 지정

