# 리스트의 값 삭제
# 1. del(리스트[인덱스]) 사용
#   인덱스를 이용해서 값을 삭제할 수 있음
#   파이썬 기본 내장 함수
#   객체를 소멸시킨다 - 없던 것으로 만든다
numList = [10, 20, 30]
# del (numList[1])
print(numList)

# 2. remove(값)
#   값을 이용해서 삭제할 수 있음
#   리스트의 함수
#   1) 값이 중복으로 여러 개 존재하면 가장 처음에 있는 값 하나만 삭제
numList = [10, 20, 30, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
numList.remove(20)
print(numList)

# 특정 값을 모두 지우고 싶으면...
for _ in range(numList.count(20)):
    numList.remove(20)
print(numList)

numList = [10, 20, 30, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
while 20 in numList:
    numList.remove(20)
print(numList)

numList = [10, 20, 30, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
if 55 in numList:
    numList.remove(55)
