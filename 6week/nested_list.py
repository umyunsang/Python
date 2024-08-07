# 리스트의 다양한 데이터 타입과 중첩 리스트 예제

# 리스트 선언 및 출력
myList = [1, 'a', [5, 6, 7]]
print(myList)  # 출력: [1, 'a', [5, 6, 7]]
print(len(myList))  # 리스트의 길이 (항목의 개수): 3

# 중첩 리스트에서 특정 요소 접근
print(myList[2][1])  # 출력: 6 (myList[2]는 [5, 6, 7]이고, 그 안에서 인덱스 1의 값은 6)

# 2차원 리스트를 반복하여 출력
numList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2중 for 루프를 사용하여 numList의 모든 요소를 출력
for n1 in numList:
    for n2 in n1:
        print(n2, end=' ')  # 요소를 공백으로 구분하여 출력
    print(' ')  # 한 행이 끝나면 줄바꿈

# 주석 처리된 코드 (같은 결과를 제공하는 다른 방법)
# for n1 in range(len(numList)):
#     for n2 in range(len(numList[n1])):
#         print(numList[n1][n2], end=' ')  # 요소를 공백으로 구분하여 출력
#     print(' ')  # 한 행이 끝나면 줄바꿈
