import random

# 문자열형으로 처리하는 방법
# 문자열 입력을 받아서 당첨 조건을 비교
lottery = input('복권번호(1-99)를 입력하시오 : ')
winner = str(random.randint(1, 99))  # 당첨 번호를 문자열로 생성

# 입력된 번호와 당첨 번호를 두 자릿수로 맞추기
if len(lottery) == 1:
    lottery = '0' + lottery
if len(winner) == 1:
    winner = '0' + winner

print(f'당첨 번호 : {winner}')
# 1등상: 번호가 완전히 일치하는 경우
if lottery == winner:
    print("1등상!")
# 2등상: 첫 번째 자릿수 또는 두 번째 자릿수가 일치하는 경우
elif lottery[0] == winner[0] or lottery[1] == winner[1]:
    print("2등상!")
else:
    print("미당첨 ㅠ")

# 숫자형으로 처리하는 방법
# 숫자 입력을 받아서 당첨 조건을 비교
lottery = int(input('복권번호(1-99)를 입력하시오 : '))
winner = random.randint(1, 99)  # 당첨 번호를 숫자로 생성

print(f'당첨 번호 : {winner}')
# 1등상: 번호가 완전히 일치하는 경우
if lottery == winner:
    print("1등상!")
# 2등상: 첫 번째 자릿수 또는 두 번째 자릿수가 일치하는 경우
elif lottery // 10 == winner // 10 or lottery % 10 == winner % 10:
    print("2등상!")
else:
    print("미당첨 ㅠ")
