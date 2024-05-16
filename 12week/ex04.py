# 숫자 x와 n을 받아
# x부터 x씩 증가하는 숫자 n개를 가진 리스트를 반환
def solution(x, n):
    # 1 ~ n까지의 수열
    # (1) 일반적인 제어문
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)

    # (2) List Comprehension
    answer = [x * i for i in range(1, n+1)]
    return answer

x_list = [2, 4, -4]
n_list = [5, 3, 2]

# (1) 인덱스를 이용해 여러 값 전달
for idx in range(len(x_list)):
    print(solution(x_list[idx], n_list[idx]))

# (2) zip 함수 => 각 리스트의 요소를 하나씩 가져와 묶어서 반환해주는 함수
for v1, v2 in zip(x_list, n_list):
    print(solution(v1, v2))


