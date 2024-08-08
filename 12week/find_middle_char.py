# 문자열 s를 입력받아 가운데 글자를 출력
# s의 길이가 홀수면 가운데 글자 하나만 반환
#           짝수면 가운데 글자 2개를 반환
def solution(s):
    """
    주어진 문자열 s의 길이에 따라 가운데 글자를 반환합니다.
    - 문자열 길이가 홀수인 경우: 가운데 글자 1개
    - 문자열 길이가 짝수인 경우: 가운데 글자 2개

    Parameters:
    s (str): 입력 문자열

    Returns:
    str: 가운데 글자
    """
    length = len(s)
    if length % 2 == 0:
        # 문자열 길이가 짝수인 경우, 가운데 2글자
        middle_index1 = length // 2 - 1
        middle_index2 = length // 2
        return s[middle_index1] + s[middle_index2]
    else:
        # 문자열 길이가 홀수인 경우, 가운데 1글자
        middle_index = length // 2
        return s[middle_index]


# 테스트 케이스
s1 = 'abcde'  # 홀수 길이: 가운데 글자 'c'
print(solution(s1))  # 결과: 'c'

s2 = 'qwer'  # 짝수 길이: 가운데 글자 'we'
print(solution(s2))  # 결과: 'we'
