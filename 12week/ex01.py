# 문자열 s에 대해서
# p와 y의 갯수를 센 다음 비교
# 갯수가 같으면 True, 아니면 False
# 1) 대소문자를 구분하지 않는다

def solution(s):
    # p와 y의 갯수 세기
    p_count = 0
    y_count = 0

    # (1)
    s = s.lower()
    for c in s:
        if c == 'p':
            p_count += 1
        if c == 'y':
            y_count += 1

    # (2)
    s = s.lower()
    p_count = s.count('p')
    y_count = s.count('y')

    # p와 y의 갯수를 비교
    # (1)
    # if p_count == y_count:
    #     return True
    # else:
    #     return False
    # (2)
    return p_count == y_count


s = 'pPoooyY'
print(solution(s))
s = 'Pyy'
print(solution(s))