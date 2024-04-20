import random

# lottery = []
#
# while len(lottery) < 6:
#     n = random.randint(1,45)
#     if n not in lottery:
#         lottery.append(n)
#
# print(lottery)

# 1 ~ 45까지의 숫자 중에 6개 뽑기
lottery_range = list(range(1, 46))
lottery = random.sample(lottery_range, 6)
print(lottery)

lottery_range = list(range(1, 46))
random.shuffle(lottery_range)
lottery = lottery_range[:6]
print(lottery)
