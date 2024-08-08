# (1) 주어진 리스트의 값을 divisor로 나누었을 때
#     나누어 떨어지는 값을 반환 리스트에 담아서 반환
# (2) 반환 리스트는 오름차순 정렬
# (3) 나누어 떨어지는 값이 없으면(= 반환 리스트의 길이가 0) [-1] 리스트를 반환
def solution(arr, divisor):
    # # (1) 주어진 리스트에서 divisor로 나누어 떨어지는 값만 필터링
    # result = []
    # for n in arr:
    #     if n % divisor == 0:
    #         result.append(n)
    # # (2) 필터링된 리스트를 오름차순으로 정렬
    # result.sort()
    #
    # # (3) 나누어 떨어지는 값이 없으면 [-1] 리스트 반환
    # if len(result) == 0:
    #     result = [-1]
    #
    # return result

    result = sorted([n for n in arr if n % divisor == 0])
    return [-1] if len(result) == 0 else result


# 테스트 케이스
arr = [[5, 9, 7, 10],
       [2, 36, 1, 3],
       [3, 2, 6]]
divisor = [5, 1, 10]

# 각 arr와 divisor 쌍에 대해 solution 함수 실행
for a, d in zip(arr, divisor):
    print(solution(a, d))



