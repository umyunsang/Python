# 딕셔너리 생성
myDict = {
    'a': 'apple',       # 문자열 키와 문자열 값
    2: 'two',           # 정수 키와 문자열 값
    '삼': 3,             # 문자열 키와 정수 값
    4: [1, 2, 3]        # 정수 키와 리스트 값
}

# 딕셔너리 출력
print(myDict)

# 딕셔너리의 값 접근
# 키 'a'에 해당하는 값 출력
print(myDict['a'])
# 키 2에 해당하는 값 출력
print(myDict[2])

# 딕셔너리의 값 수정
# 키 '삼'에 해당하는 값을 300으로 수정
myDict['삼'] = 300
print(myDict)

# 딕셔너리의 아이템 추가
# 키 '오'에 새로운 값 500 추가
myDict['오'] = 500
print(myDict)

# 딕셔너리의 아이템 삭제
# 키 '삼'에 해당하는 아이템 삭제
del(myDict['삼'])
print(myDict)

# 딕셔너리의 순회
# 키와 값 쌍을 출력
for k, v in myDict.items():
    print(f'키 : {k} / 값 : {v}')
