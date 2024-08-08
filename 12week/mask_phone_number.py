# 문자열 숫자가 주어졌을 때 맨 뒤 4자리만 남기고 나머지는 '*'
def solution(phone_number):
    # (1) 문자열을 리스트로 바꾼 후에 조정
    # 문자열을 리스트로 변환하여 각 문자에 접근 가능
    result = list(phone_number)

    # 맨 뒤 4자리를 제외한 나머지를 '*'로 변경
    for idx in range(len(result) - 4):
        result[idx] = '*'

    # 리스트를 문자열로 다시 변환
    result = ''.join(result)

    # (2) 문자열 슬라이싱을 이용한 방법
    # 전화번호의 맨 뒤 4자리와 그 전의 부분으로 나누기
    front = phone_number[:-4]  # 전화번호의 맨 뒤 4자리를 제외한 부분
    back = phone_number[-4:]  # 전화번호의 맨 뒤 4자리

    # 앞부분은 '*'로 채우고 뒤 4자리는 그대로 붙여서 결과 생성
    result = '*' * len(front) + back

    return result


# 테스트 케이스
phone_number = ["01033334444", "027778888"]

# 각 전화번호에 대해 solution 함수 실행
for p in phone_number:
    print(solution(p))  # 결과: 0103333****, ****8888
