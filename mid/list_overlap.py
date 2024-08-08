# 두 개의 리스트 정의
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]

same_val = False  # 공통된 값이 있는지 여부를 저장할 변수

# list1의 각 요소에 대해
for n1 in list1:
    if n1 in list2:  # list2에 n1이 존재하는지 확인
        same_val = True  # 공통된 값이 있으면 True로 설정
        break  # 첫 번째 공통값을 찾으면 루프 종료

# 결과 출력
print(same_val)
