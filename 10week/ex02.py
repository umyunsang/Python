# List Comprehension
# 리스트를 생성하는 방법 중 하나
# 빈 리스트를 먼저 만들고, 반복문을 통해서 리스트이 값을 채우는 작업

# 예) 3의 배수 8개를 갖는 리스트를 만들어야 할 때
my_list = []
for x in range(1, 9):
    my_list.append(x * 3)
print(my_list)

my_list = [x * 3 for x in range(1, 9)]  # List Comprehension
print(my_list)

