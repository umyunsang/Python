# 문자열 s를 입력받아 가운데 글자를 출력
# s의 길이가 홀수면 가운데 글자 하나만 반환
#           짝수면 가운데 글자 2개를 반환
def solution(s):
    msg = '' if len(s) % 2 == 0 else s[len(s) // 2 - 1]
    msg += s[len(s) // 2]
    return msg

    # if len(s) % 2 != 0:
    #     return s[len(s) // 2]
    # else:
    #     return s[len(s) // 2 - 1] + s[len(s) // 2]


s = 'abcde' # 'c' -> s[2]    len(s)//2
print(solution(s))
s = 'qwer'  # 'we' -> s[1] + s[2]      len(s)//2 - 1, len(s)//2
print(solution(s))