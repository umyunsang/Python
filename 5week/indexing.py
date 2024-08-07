# 리스트를 생성하고 초기화
num_list = [0, 0, 0, 0]
print(len(num_list))  # 리스트의 길이(요소의 개수)를 출력

# 사용자로부터 입력을 받아 리스트의 값을 수정하기 위한 주석 처리된 부분
# for i in num_list:
#     i = int(input('숫자 : '))
#
# print(num_list)

# 인덱스를 이용하여 num_list에 직접 접근하여 값을 수정
for i in range(len(num_list)):  # len(num_list)는 4, 따라서 range(len(num_list))는 [0, 1, 2, 3]을 생성
    num_list[i] = int(input('숫자 : '))  # 각 인덱스에 대해 사용자로부터 숫자를 입력받아 리스트의 값을 수정

print(num_list)  # 수정된 리스트를 출력

# 인덱스를 이용한 값 접근 및 총합 계산
hap = 0
for i in range(len(num_list)):  # 인덱스를 사용하여 리스트의 각 요소를 순회
    hap += num_list[i]  # 각 요소를 hap에 더함
print(f'총합 : {hap}')  # 총합을 출력

# 리스트의 값을 직접 순회하여 총합 계산
hap = 0
for n in num_list:  # 리스트의 각 요소를 직접 순회
    hap += n  # 각 요소를 hap에 더함
print(f'총합 : {hap}')  # 총합을 출력
