def solution(s):
    # p와 y의 갯수 세기 초기화
    p_count = 0
    y_count = 0

    # 대소문자 구분하지 않기 위해 문자열을 모두 소문자로 변환
    s = s.lower()

    # (1) for 루프를 통해 문자열에서 p와 y의 개수를 센다
    for c in s:
        if c == 'p':
            p_count += 1
        if c == 'y':
            y_count += 1

    # (2) 문자열 메서드를 사용하여 p와 y의 개수를 센다
    # 위의 방법보다 더 간결하고 파이썬다운 방법
    p_count = s.count('p')
    y_count = s.count('y')

    # p와 y의 갯수를 비교하여 같으면 True, 다르면 False 반환
    return p_count == y_count

# 테스트 케이스
s = 'pPoooyY'
print(solution(s))  # True
s = 'Pyy'
print(solution(s))  # False
