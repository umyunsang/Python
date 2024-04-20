'''
요구사항:
1.주문된 모든 음식의 총 가격을 계산하세요.
2.가장 많이 주문된 음식과 그 주문 횟수를 찾으세요.

주어진 데이터:
food_price = [1200, 1500, 1800, 1000] # 김방(0), 라면(1), 돈까스(2), 샐러드(3)
order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]

출력:
총 가격: 23300원/가장 많이 주무된 음식 : 라면, 5회
'''

# 김방(0), 라면(1), 돈까스(2), 샐러드(3)
food_price = [1200, 1500, 1800, 1000]
order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]
total = 0
order_cnt = [0] * len(food_price)

for order in order_history:
    total += food_price[order]
    order_cnt[order] += 1
print(f'총 가격 : {total}')
print(f'메뉴 주문 횟수 : {order_cnt}')

# 가장 많이 주문된 횟수(max)
max_cnt = max(order_cnt)
print(f'가장 많이 주문된 횟수 : {max_cnt}')

best_foods = []
food_names = ['김밥', '라면', '돈가스', '샐러드']
for idx in range(len(order_cnt)):
    if order_cnt[idx] == max_cnt:
        best_foods.append(food_names[idx])
print(f'가장 많이 주문된 음식 : {best_foods}')

print(f'총 가격: {total}원 / 가장 많이 주문된 음식:',end='')
for f in best_foods:
    print(f'{f}',end='')
print(f'{max_cnt}회')



# food_price = {'김밥': 1200, '라면': 1500, '돈까스': 1800, '샐러드': 1000}
# order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]
#
# # 1. 주문된 모든 음식의 총 가격 계산
# total_price = 0
# for food_idx in order_history:
#     total_price += food_price[list(food_price.keys())[food_idx]]
#
# # 2. 가장 많이 주문된 음식과 주문 횟수 찾기
# order_count = {}
# for food_idx in order_history:
#     food_name = list(food_price.keys())[food_idx]
#     order_count[food_name] = order_count.get(food_name, 0) + 1
#
# max_order_food = max(order_count, key=order_count.get)
# max_order_count = order_count[max_order_food]
#
# # 결과 출력
# print(f"총 가격: {total_price}원")
# print(f"가장 많이 주문된 음식: {max_order_food}, {max_order_count}회")
