# 문자열 리스트 정의
myList = ['aba', 'xyz', 'abc', '121']
same_count = 0  # 동일한 첫 문자와 끝 문자의 개수를 저장할 변수

# 각 문자열의 첫 문자와 끝 문자를 비교
for word in myList:
    if word[0] == word[-1]:  # 첫 문자와 끝 문자가 동일한지 확인
        same_count += 1  # 동일한 경우 개수 증가

# 결과 출력
print(f'문자열의 개수 = {same_count}')
