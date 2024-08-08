# 숫자 x와 n을 받아
# x부터 x씩 증가하는 숫자 n개를 가진 리스트를 반환
def solution(x, n):
    # x부터 x씩 증가하는 숫자 n개를 가진 리스트 생성

    # (1) 일반적인 제어문 사용
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)

    # (2) List Comprehension 사용
    answer = [x * i for i in range(1, n + 1)]

    return answer


# 테스트 케이스
x_list = [2, 4, -4]
n_list = [5, 3, 2]

# (1) 인덱스를 이용해 여러 값 전달
print("Using index:")
for idx in range(len(x_list)):
    print(solution(x_list[idx], n_list[idx]))

# (2) zip 함수를 사용하여 각 리스트의 요소를 하나씩 가져와 묶어서 전달
print("Using zip:")
for v1, v2 in zip(x_list, n_list):
    print(solution(v1, v2))
