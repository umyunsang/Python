# 숫자 n을 받아서 각 자릿수를 내림차순으로 정렬한 숫자를 반환
def solution(n):
    # 숫자를 문자열로 변환하고 각 자릿수를 리스트로 저장
    nl = list(str(n))

    # 각 자릿수를 내림차순으로 정렬
    nl.sort(reverse=True)

    # 정렬된 리스트를 문자열로 변환
    msg = ''.join(nl)

    # 문자열을 정수로 변환하여 반환
    result = int(msg)

    return result


def solution1(n):
    # 숫자를 문자열로 변환, 정렬, 다시 문자열로 합치고, 정수로 변환
    return int(''.join(sorted(str(n), reverse=True)))


# 테스트 케이스
n = 118372
print(solution(n))  # 873211
print(solution1(n))  # 873211
