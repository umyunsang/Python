
print("## 택배를 보내기 위한 정보를 입력하세요. ##")
name = input("받는 사람 : ")
address = input("주소 : ")
gram = int(input("무게(g) : "))

print("** 받는 사람 ==>",name)
print("** 주소 ==>" +address)
print(f'** 배송비 ==>" {gram * 5} 원')
