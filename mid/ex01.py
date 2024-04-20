myList = ['aba','xyz','abc','121']
same_count = 0

# 각 문자열의 첫 문자와 끝 문자
for word in myList:
    if word[0] == word[-1]:
        same_count += 1

print(f'문자열의 개수 = {same_count}')