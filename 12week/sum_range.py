# 정수 a, b를 받아서 a부터 b까지의 숫자 합
# a와 b의 대소관계는 정해져있지 않다

def solution(a, b):
    # a와 b의 대소 관계에 상관없이 범위를 정렬하여 a가 작은 값이 되도록 설정
    if a > b:
        a, b = b, a

    # a와 b를 범위에 맞게 정렬한 후 사용
    # (a, b) = (b, a) if a > b else (a, b)  # 중복 코드 제거
    # (a, b) = (b, a) if a > b else (a, b)  # 중복 코드 제거

    # a부터 b까지의 숫자를 모두 더하기 위한 초기화
    hap = 0

    # a부터 b까지 반복하며 합계를 계산
    for i in range(a, b + 1):
        hap += i

    # list(range(a, b+1))를 사용하여 범위 내의 모든 숫자를 리스트로 만든 후 합계를 계산
    hap = sum(range(a, b + 1))

    return hap

# 테스트 케이스
a_list = [3, 3, 5]
b_list = [5, 3, 3]

# 각 a와 b 값에 대해 solution 함수 실행
for v1, v2 in zip(a_list, b_list):
    print(solution(v1, v2))  # 출력 결과: 12, 12, 5
