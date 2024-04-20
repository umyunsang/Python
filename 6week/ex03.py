myDict = {'a': 'apple',
          2: 'two',
          '삼': 3,
          4: [1, 2, 3]}

print(myDict)

# 딕셔너리의 값 접근 ==> 딕셔너리[키]
print(myDict['a'])
print(myDict[2])

# 딕셔너리의 값 수정 ==> 딕셔너리[키] = 새로운 값
myDict['삼'] = 300
print(myDict)

# 딕셔너리의 아이템 추가 ==> 딕셔너리[키] = 새로운 값
myDict['오'] = 500
print(myDict)

# 딕셔너리의 아이템 삭제
del(myDict['삼'])
print(myDict)

# 딕셔너리의 순회
for k, v in myDict.items():
    print(f'키 : {k} / 값 : {v}')