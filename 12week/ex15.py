# 문자열 s의 길이가 4 혹은 6
# 숫자로만 구성돼있는지 확인

def solution(s):
    # s = 'a234'
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

s = 'a234'
print(solution(s))
s = '1234'
print(solution(s))
s = '12345'
print(solution(s))