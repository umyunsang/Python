# 하샤드수 판별 문제
# 숫자 x를 받고, x가 각 자릿수의 합으로 나누었을 때 나머지가 0이면 True

def solution(x):
    # 각 자릿수의 합
    # (1) 수학적인 접근
    # hap = 0
    # tmp = x
    # while tmp != 0:
    #     hap += tmp % 10  # 1의 자릿수 누적
    #     tmp = tmp // 10  # 1의 자릿수 탈락

    # (2) 파이썬의 문자열과 리스트 변환의 특징을 이용한 방법
    msg = str(x)  # int to string
    nl = list(msg) # string to list

    # (2-1)
    # hap = 0
    # for n in nl:
    #     hap += int(n)

    # (2-2)
    # map 함수
    # map(함수, 리스트) => 리스트에 있는 각 요소들에 함수를 적용한 map 객체를 반환
    nl = list(map(int, nl))
    hap = sum(nl)

    # x % 각 자릿수의 합 == 0 ?
    return x % hap == 0


arr = [10, 12, 11, 13]
for a in arr:
    print(solution(a))