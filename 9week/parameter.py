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
# 파라미터에 대한 다양한 사용법을 설명하는 예제

# 1. 기본값을 가지는 파라미터
# 기본값이 지정된 파라미터는 함수 호출 시 해당 인자가 제공되지 않으면 기본값이 사용됩니다.
def hap_func1(v1, v2=5):  # v2의 기본값을 5로 설정
    hap = v1 + v2
    print(f'{hap}')  # 합계 출력

hap_func1(10)  # v2를 제공하지 않으면 기본값 5가 사용됨
hap_func1(10, 3)  # v2에 3을 전달하여 결과를 출력

# 기본값이 있는 파라미터와 없는 파라미터를 함께 사용하는 함수
def hap_func2(v1, v2, v3=0, v4=0, v5=0):
    hap = v1 + v2 + v3 + v4 + v5
    print(f'{hap}')  # 합계 출력

hap_func2(1, 2)  # v3, v4, v5의 기본값 0이 사용됨
hap_func2(1, 2, 3, 4, 5)  # 모든 인자를 제공하여 결과를 출력

# 2. 리스트 또는 튜플을 사용하여 여러 값을 전달
# 리스트 또는 튜플을 사용하여 가변적인 수의 인자를 처리할 수 있음
def hap_func3(nums):  # nums는 리스트 또는 튜플
    hap = sum(nums)  # 리스트의 합계를 계산
    print(f'hap_func3 : {hap}')  # 합계 출력

hap_func3([1, 2, 3, 5, 3, 2])  # 리스트를 인자로 전달

# 3. 가변 길이 파라미터 (튜플)
# 함수가 여러 개의 인자를 받을 수 있도록 해줍니다.
def hap_func4(*nums):  # *nums는 가변 길이 인자를 받음
    print(nums)  # 전달된 인자들을 튜플 형태로 출력
    print(type(nums))  # nums의 타입 확인 (튜플)
    hap = sum(nums)  # 튜플의 합계를 계산
    print(f'hap_func4 : {hap}')  # 합계 출력

hap_func4(4, 9, 12)  # 여러 개의 인자를 전달

# 가변 길이 파라미터는 항상 함수 정의에서 마지막에 와야 합니다.
def hap_func5(v1, v2, *nums1):  # *nums1은 가변 길이 인자를 받음
    hap1 = sum(nums1)  # nums1의 합계를 계산
    print(f'hap_func5 : {hap1}')  # 합계 출력

hap_func5(1, 2, 3, 4, 5, 6, 7)  # v1, v2와 가변 길이 인자를 전달

# 기본값이 지정된 파라미터는 항상 일반 파라미터보다 뒤에 와야 합니다.
def hap_func6(v1, v3, v2=5):  # 기본값이 있는 파라미터 v2는 뒤에 위치
    hap = v1 + v2 + v3
    print(f'hap_func6 : {hap}')  # 합계 출력

hap_func6(2, 5)  # 기본값 5가 사용됨
hap_func6(v1=2, v2=6, v3=11)  # 파라미터의 이름을 명시하여 호출


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

