total = 0
a = int(input("여행자 총 인원 수 : "))
b = int(input("숙박비용 : "))
total += b
c = int(input("식비 : "))
total += c
d = int(input("기타 경비 : "))
total += d

print(f'전체 여행 경비는 {total}원이며, 인원 수가 {a}명 일 때, 각자 금액 : {total/a}원')
