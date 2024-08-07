# 음식 가격 리스트 (인덱스: 음식 종류)
# 김밥(0), 라면(1), 돈까스(2), 샐러드(3)
food_price = [1200, 1500, 1800, 1000]

# 주문 기록 리스트 (값: 음식 종류의 인덱스)
order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]

# 총 가격 계산 변수 초기화
total = 0

# 각 음식의 주문 횟수를 기록할 리스트 초기화
order_cnt = [0] * len(food_price)  # [0, 0, 0, 0] (4종의 음식이므로 4개의 0으로 초기화)

# 주문 기록을 순회하며 총 가격 계산 및 주문 횟수 업데이트
for order in order_history:
    total += food_price[order]  # 주문된 음식의 가격을 총 가격에 추가
    order_cnt[order] += 1       # 해당 음식의 주문 횟수 증가

# 총 가격 출력
print(f'총 가격 : {total}')

# 각 음식의 주문 횟수 출력
print(f'메뉴 주문 횟수 : {order_cnt}')

# 가장 많이 주문된 횟수 찾기
max_cnt = max(order_cnt)
print(f'가장 많이 주문된 횟수 : {max_cnt}')

# 가장 많이 주문된 음식 찾기
best_foods = []
food_names = ['김밥', '라면', '돈가스', '샐러드']
for idx in range(len(order_cnt)):
    if order_cnt[idx] == max_cnt:
        best_foods.append(food_names[idx])

# 결과 출력
print(f'총 가격: {total}원 / 가장 많이 주문된 음식:', end='')
for f in best_foods:
    print(f'{f}', end='')
print(f'{max_cnt}회')
