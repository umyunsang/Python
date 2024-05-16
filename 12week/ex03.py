# 숫자 n을 받아서 각 자릿수를 내림차순으로 정렬한 숫자를 반환
def solution(n):
    # 각 자릿수를 내림차순으로 정렬
    nl = list(str(n))
    nl.sort(reverse=True)

    # list<string> to string
    # msg = ''
    # for c in nl:
    #     msg += c
    msg = ''.join(nl)

    # string to integer
    result = int(msg)

    return result


n = 118372
print(solution(n))