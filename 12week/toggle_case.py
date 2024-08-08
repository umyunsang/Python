# 각 단어의 짝수번째 인덱스 문자를 대문자로
# 홀수번째 인덱스 문자를 소문자로 변환하는 함수

def solution(s):
    # 문자열을 공백을 기준으로 나누어 단어 리스트를 생성
    words = s.split(' ')

    # 변환된 단어들을 저장할 리스트
    result = []

    # 각 단어에 대해 처리
    for word in words:
        msg = ''  # 변환된 단어를 저장할 변수
        for idx in range(len(word)):
            # 짝수번째 인덱스는 대문자
            if idx % 2 == 0:
                msg += word[idx].upper()
            # 홀수번째 인덱스는 소문자
            else:
                msg += word[idx].lower()
        # 변환된 단어를 결과 리스트에 추가
        result.append(msg)

    # 결과 리스트를 공백으로 구분하여 문자열로 변환
    result = ' '.join(result)
    return result


# 테스트 케이스
s = "try hello world"
print(solution(s))
