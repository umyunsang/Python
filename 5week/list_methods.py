# pop() 메소드
# 리스트의 마지막 요소를 제거하고 그 값을 반환합니다.
numList = [10, 20, 30]
numList.pop()  # 마지막 요소 30을 제거
print(numList)  # 출력: [10, 20]

# sort() 메소드
# 리스트의 요소를 정렬합니다. 리스트 자체를 수정하며 반환값은 없음.
numList = [99, 24, 58, 42, 10]
numList.sort()  # 리스트를 오름차순으로 정렬
print(numList)  # 출력: [10, 24, 42, 58, 99]

# sorted() 함수
# 리스트를 정렬하여 새로운 리스트를 반환합니다. 원본 리스트는 변경되지 않음.
numList = [99, 24, 58, 42, 10]
numList = sorted(numList)  # 새로운 정렬된 리스트를 반환
print(numList)  # 출력: [10, 24, 42, 58, 99]

# sorted() 함수를 문자열 리스트에 적용
numList = ['다람쥐', '기러기', '나비']
numList = sorted(numList)  # 새로운 정렬된 리스트를 반환
print(numList)  # 출력: ['기러기', '나비', '다람쥐']

# reverse() 메소드
# 리스트의 요소를 역순으로 뒤집습니다. 리스트 자체를 수정하며 반환값은 없음.
numList = [10, 20, 30, 40, 50, 60]
numList.reverse()  # 리스트를 역순으로 정렬
print(numList)  # 출력: [60, 50, 40, 30, 20, 10]

# copy() 메소드
# 리스트의 얕은 복사본을 반환합니다. 깊은 복사와 유사하지만 복사본과 원본은 독립적입니다.
numList = [10, 20, 30]
numList2 = numList.copy()  # 깊은 복사(Deep copy): 두 변수는 독립체
# numList2 = numList[:]    # 동일한 효과를 제공
# numList2 = numList       # 얕은 복사(Swallow copy): 두 변수가 동일함
numList2[1] = 999  # 복사본에서 값 수정
print(numList)  # 출력: [10, 20, 30]
print(numList2)  # 출력: [10, 999, 30]
