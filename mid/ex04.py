import random

# 문자열형으로 다룰지 (사전처리 필요, 당첨조건 비교가 쉬움)
lottery = input('복권번호(1-99)를 입력하시오 : ')
winner = str(random.randint(1,99))

if len(lottery) == 1:
    lottery = '0' + lottery
if len(winner) == 1:
    winner = '0' + winner

print(f'당첨 번호 : {winner}')
if lottery == winner:
    print("1등상!")
elif lottery[0] == winner[0] or lottery[1] == lottery[1]:
    print("2등상!")
else:
    print("미당첨 ㅠ")

# 숫자형으로 다룰지 (사전처리 x, 당첨조건비교가 살짝 까다로움)
lottery = int(input('복권번호(1-99)를 입력하시오 : '))
winner = random.randint(1,99)

print(f'당첨 번호 : {winner}')
if lottery == winner:
    print("1등상!")
elif lottery//10 == winner //10 or lottery % 10 == winner % 10:
    print("2등상!")
else:
    print("미당첨 ㅠ")