# 슬라이싱(slicing)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 기분 문법
# 리스트[시작인덱스 : 끝인덱스] : 시작인덱스 ~ (끝인덱스 -1) 까지의 값을 복사
new_list1 = my_list[2:7]
print(new_list1)
new_list2 = my_list[5:6]
print(new_list2)
new_list3 = my_list[5:5]
print(new_list3)

# 시작인덱스를 생략하면 리스트와 처음부터 끝인덱스-1 까지
new_list4 = my_list[:5]
print(new_list4)

# 끝 인덱스를 생략하면 시작인덱스 부터 리스트 끝까지
new_list5 = my_list[5:]
print(new_list5)

# 둘다 생략
# 완전 독립 복사 (hardcopy) : 원본과 복사체가 서로 같은 정보를 가지지만 연관이 없음
new_list6 = my_list[:]
print(new_list6)