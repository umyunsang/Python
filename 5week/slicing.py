# 슬라이싱(slicing) 예제
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 기본 문법: 리스트[시작인덱스 : 끝인덱스]
# 끝인덱스는 슬라이스 결과에 포함되지 않음

# 시작인덱스가 2, 끝인덱스가 7인 슬라이스
new_list1 = my_list[2:7]
print(new_list1)  # 출력: [2, 3, 4, 5, 6]

# 시작인덱스가 5, 끝인덱스가 6인 슬라이스
new_list2 = my_list[5:6]
print(new_list2)  # 출력: [5]

# 시작인덱스와 끝인덱스가 동일할 경우 빈 리스트 반환
new_list3 = my_list[5:5]
print(new_list3)  # 출력: []

# 시작인덱스를 생략하면 리스트의 처음부터 끝인덱스-1까지 슬라이스
new_list4 = my_list[:5]
print(new_list4)  # 출력: [0, 1, 2, 3, 4]

# 끝인덱스를 생략하면 시작인덱스부터 리스트의 끝까지 슬라이스
new_list5 = my_list[5:]
print(new_list5)  # 출력: [5, 6, 7, 8, 9]

# 둘 다 생략하면 리스트의 전체 복사
# 원본과 복사체가 서로 같은 정보를 가지지만 서로 독립적임 (hardcopy)
new_list6 = my_list[:]
print(new_list6)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
