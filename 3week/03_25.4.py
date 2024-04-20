# 1.사용자의 대출 가능한 책의 수는 최대 3권입니다.
# 2. 책을 대출하기 위해서 사용자의 등급이 골드 아님 실버
# 3. 브론즈는 절대 대출 금지
# 4.특별 이벤트 기간에 모든 회원 책 추가로 1권 더 대출

book = int(input('현재 대출하고 있는 책의 수 : '))
grade = input("회원 등급 : ")
event = input("특별 이벤트 기간인가요? (예/아니요) : ")

if grade == '브론즈':
    print("브론즈 등급은 대출이 불가합니다.")
else:
    r_book = 3
    if event == '예':
        r_book += 1
    r_book -= book
    if r_book <= 0:
        print("더 이상 대출할 수 없습니다.")
    else:
        print(f'추가로 {r_book}권 대출 가능합니다.')


