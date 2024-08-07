# 빈 리스트를 생성하는 두 가지 방법

# 1. 대괄호를 사용한 빈 리스트 생성
my_list = []
print(my_list)  # 출력: []

# 2. list() 생성자를 사용한 빈 리스트 생성
my_list2 = list()
print(my_list2)  # 출력: []

# 리스트를 값과 함께 초기화
my_list3 = [2, 5, 4]
print(my_list3)  # 출력: [2, 5, 4]

# 리스트의 인덱스를 사용하여 개별 요소에 접근
print(my_list3[0])  # 출력: 2
print(my_list3[1])  # 출력: 5
print(my_list3[2])  # 출력: 4

# 리스트의 모든 요소를 순회하며 출력
for i in my_list3:
    print(i)  # 출력: 2, 5, 4 (각각 한 줄씩)
