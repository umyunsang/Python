num_list = [0, 0, 0, 0]
print(len(num_list))


# for i in num_list:
#     i = int(input('숫자 : '))
#
# print(num_list)

# 인덱스를 이용해 num_list에 직접 접근하여 값을 수정
for i in range(len(num_list)):  # 인덱스에 해당하는 0 ~ 3의 수열이 필요
    num_list[i] = int(input('숫자 : '))

print(num_list)

# 인덱스를 이용한 값 접근
hap = 0
for i in range(len(num_list)):
    hap += num_list[i]
print(f'총합 : {hap}')

# 리스트의 값 대입을 이용한 방법
hap = 0
for n in num_list:
    hap += n
print(f'총합 : {hap}')