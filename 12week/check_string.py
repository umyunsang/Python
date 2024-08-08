def solution(s):
    """
    주어진 문자열 s가 길이가 4 또는 6인지, 그리고 숫자로만 구성되어 있는지를 확인합니다.

    Parameters:
    s (str): 확인할 문자열

    Returns:
    bool: 조건을 만족하면 True, 그렇지 않으면 False
    """

    # 문자열 길이가 4 또는 6인지 확인하고, 숫자만으로 구성되어 있는지 확인
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False


# 테스트 케이스
s = 'a234'
print(solution(s))  # 예상 결과: False, 문자열에 숫자가 아닌 문자가 포함되어 있음

s = '1234'
print(solution(s))  # 예상 결과: True, 문자열의 길이가 4이고 숫자로만 구성됨

s = '12345'
print(solution(s))  # 예상 결과: False, 문자열의 길이가 5로 조건을 만족하지 않음
