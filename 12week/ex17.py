# 각 단어의 짝수번째 인덱스 문자를 대문자
#          홀수번째 인덱스 문자를 소문자
def solution(s):
    # 문자열.split(구분문자) => 문자열을 구분문자를 기준으로 분리 / 결과는 리스트에 담음
    words = s.split(' ')
    result = []

    for word in words:
        msg = ''
        for idx in range(len(word)):
             if idx % 2 == 0:
                 msg += word[idx].upper()
             else:
                 msg += word[idx].lower()
        result.append(msg)

    result = ' '.join(result)
    return result


s = "try hello world"
print(solution(s))