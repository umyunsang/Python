# 하샤드수 판별 문제
# 숫자 x를 받고, x가 각 자릿수의 합으로 나누었을 때 나머지가 0이면 True

def solution(x):
    # 각 자릿수의 합을 계산

    # (1) 수학적인 접근
    # 숫자를 한 자리씩 분리하여 합을 구함
    # hap = 0
    # tmp = x
    # while tmp != 0:
    #     hap += tmp % 10  # 1의 자릿수를 더함
    #     tmp = tmp // 10  # 1의 자릿수를 제거

    # (2) 파이썬의 문자열과 리스트 변환을 이용한 방법
    # 숫자를 문자열로 변환하여 각 자릿수를 리스트로 변환
    msg = str(x)  # int를 string으로 변환
    nl = list(msg) # string을 list로 변환

    # (2-1) for 루프를 통해 각 자릿수를 더하는 방법
    # hap = 0
    # for n in nl:
    #     hap += int(n)

    # (2-2) map 함수를 이용한 방법
    # map(함수, 리스트) => 리스트에 있는 각 요소들에 함수를 적용한 map 객체를 반환
    nl = list(map(int, nl))  # 리스트의 각 요소를 int로 변환
    hap = sum(nl)  # 각 자릿수의 합을 계산

    # x를 각 자릿수의 합으로 나눈 나머지가 0인지 확인
    return x % hap == 0

# 테스트 케이스
arr = [10, 12, 11, 13]
for a in arr:
    print(solution(a))  # True, True, False, False
