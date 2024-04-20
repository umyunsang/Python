# pop()
numList = [10, 20, 30]
numList.pop()
print(numList)

# sort() - 리스트의 함수 -> return X
numList = [99, 24, 58, 42, 10]
numList.sort()
print(numList)

# sorted() - 파이썬의 기본 내장 함수 -> return O
numList = [99, 24, 58, 42, 10]
numList = sorted(numList)
print(numList)
numList = ['다람쥐', '기러기', '나비']
numList.sort()
print(numList)

# reverse()
numList = [10, 20, 30, 40, 50, 60]
numList.reverse()
# numList = numList[::-1]
print(numList)

# copy()
numList = [10, 20, 30]
numList2 = numList.copy()   # 깊은 복사(Deep,hard copy) : 두 변수는 독립체
# numList2 = numList[:]     # 이하 동일
# numList2 = numList        # 얕은 복사(Swallow copy) : 두 변수가 동일함
numList2[1] = 999
print(numList)
print(numList2)

