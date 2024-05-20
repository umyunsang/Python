# 문자열 숫자가 주어졌을 때 맨 뒤 4자리만 남기고 나머지는 '*'
def solution(phone_number):
    # (1) 문자열을 리스트로 바꾼 후에 조정
    result = list(phone_number)
    for idx in range(len(result)-4):
        result[idx] = '*'
    result = ''.join(result)

    # (2) 문자열 슬라이싱, 연산
    front = phone_number[:-4]
    back = phone_number[-4:]
    result = '*' * len(front) + back
    return result


phone_number = ["01033334444", "027778888"]
for p in phone_number:
    print(solution(p))