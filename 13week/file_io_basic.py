# 파일 열기
# open(파일경로, 모드, encoding='UTF-8')
# 모드:
# - 'r': 읽기 모드 (파일이 존재해야 함)
# - 'w': 쓰기 모드 (파일이 존재하지 않으면 새로 생성, 존재하면 덮어씀)
# - 'a': 추가 모드 (파일이 존재하지 않으면 새로 생성, 존재하면 파일의 끝에 추가)

# 같은 파일에 대해...
# A 프로그램이 파일을 읽고 있는 동안 (모드 'r'):
# - B 프로그램은 읽을 수 있음 (모드 'r', 'w', 'a')
# A 프로그램이 파일을 쓰고 있는 동안 (모드 'w', 'a'):
# - B 프로그램은 읽을 수 없음 (모드 'r', 'w', 'a')
# A 프로그램이 파일을 읽고 있는 동안 (모드 'r'):
# - B 프로그램은 파일을 수정할 수 없음 (모드 'w', 'a')

# 파일 읽기
# readline() : 파일에서 한 줄을 읽어 반환
# readlines() : 파일의 모든 줄을 읽어서 리스트로 반환
# - 개행 문자가 포함되므로 필요시 strip() 함수로 제거

# 파일 쓰기
# write(문자열) : 문자열을 파일에 쓴다 (자동 개행 없음)
# writelines(문자열 리스트) : 리스트에 있는 문자열을 파일에 쓴다 (자동 개행 없음)

# 파일 닫기
# close() : 열린 파일을 닫는다 (리소스 해제)

# 예제 코드:
# 파일 쓰기
fp = open('example.txt', 'w', encoding='UTF-8')
fp.write('Hello, world!\n')
fp.writelines(['This is a line.\n', 'This is another line.\n'])
fp.close()

# 파일 읽기
fp = open('example.txt', 'r', encoding='UTF-8')
print(fp.readline().strip())  # 한 줄 읽기
print(fp.readlines())  # 모든 줄 읽기
fp.close()
