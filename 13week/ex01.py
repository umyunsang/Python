# open 함수는 운영체제의 기본 인코딩/디코딩 규칙을 따라감
# cp949 또는 x-windows-949 코딩은 '한글' 윈도우 전용
# 근데 PyCharm은 기본적으로 UTF-8 코딩방식을 사용
fp = open('myfile.txt', 'r', encoding='UTF-8')

# strip() : 문자열 뒤에 있는 공백 자름
msg = fp.readline().strip()
print(msg)
msg = fp.readline()
print(msg)
msg = fp.readline()
print(msg)

fp.close()

fp = open('myfile.txt', 'r', encoding='UTF-8')

while True:
    msg = fp.readline()
    if msg == '':
        break
    else:
        msg = msg.strip()
        print(msg)

fp.close()

fp = open('myfile.txt', 'r', encoding='UTF-8')
line_count = len(fp.readlines())
fp.seek(0)
for _ in range(line_count):
    msg = fp.readline().strip()
    print(msg)

fp.close()