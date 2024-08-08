import random

# 방법 1: random.sample() 사용하기
# random.sample()을 사용하여 1부터 45까지의 숫자 중 6개를 무작위로 선택
lottery_range = list(range(1, 46))  # 1부터 45까지의 숫자 리스트 생성
lottery = random.sample(lottery_range, 6)  # 리스트에서 6개의 숫자를 랜덤으로 선택
print("랜덤 샘플:", lottery)

# 방법 2: random.shuffle() 사용하기
# random.shuffle()을 사용하여 리스트를 무작위로 섞은 후, 처음 6개의 숫자를 선택
lottery_range = list(range(1, 46))  # 1부터 45까지의 숫자 리스트 생성
random.shuffle(lottery_range)  # 리스트를 무작위로 섞음
lottery = lottery_range[:6]  # 섞인 리스트의 처음 6개 숫자를 선택
print("랜덤 셔플:", lottery)
