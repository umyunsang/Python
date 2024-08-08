# open 함수는 운영체제의 기본 인코딩/디코딩 규칙을 따라감
# cp949 또는 x-windows-949 코딩은 '한글' 윈도우 전용
# 근데 PyCharm은 기본적으로 UTF-8 코딩방식을 사용

# 파일을 UTF-8 인코딩 방식으로 읽기
fp = open('myfile.txt', 'r', encoding='UTF-8')

# 파일의 첫 번째 줄을 읽고, 양쪽 공백을 제거한 후 출력
msg = fp.readline().strip()
print(msg)

# 파일의 두 번째 줄을 읽고, 출력 (공백 제거 없음)
msg = fp.readline()
print(msg)

# 파일의 세 번째 줄을 읽고, 출력 (공백 제거 없음)
msg = fp.readline()
print(msg)

# 파일 닫기
fp.close()

# 파일을 UTF-8 인코딩 방식으로 읽기
fp = open('myfile.txt', 'r', encoding='UTF-8')

# 파일의 끝에 도달할 때까지 한 줄씩 읽고 출력
while True:
    msg = fp.readline()
    if msg == '':  # 빈 문자열이면 파일의 끝
        break
    else:
        msg = msg.strip()  # 양쪽 공백 제거
        print(msg)

# 파일 닫기
fp.close()

# 파일을 UTF-8 인코딩 방식으로 읽기
fp = open('myfile.txt', 'r', encoding='UTF-8')

# 파일의 모든 줄을 읽어 리스트로 저장하고 줄 수 계산
line_count = len(fp.readlines())

# 파일 포인터를 처음으로 되돌림
fp.seek(0)

# 각 줄을 읽고, 양쪽 공백을 제거한 후 출력
for _ in range(line_count):
    msg = fp.readline().strip()
    print(msg)

# 파일 닫기
fp.close()
