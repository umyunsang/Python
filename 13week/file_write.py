# 'newfile.txt' 파일을 쓰기 모드('w')로 열기
# UTF-8 인코딩 방식 사용
fp = open('newfile.txt', 'w', encoding='UTF-8')

# write() : 문자열을 파일에 쓴다. 개행이 자동으로 되지 않으므로 직접 \n을 추가해줘야 한다.
fp.write('안녕')
fp.write('하세요\n')

# writelines() : 문자열 리스트를 파일에 쓴다.
# 리스트의 각 문자열 사이에 자동으로 개행이 추가되지 않으므로 개행이 필요하면 직접 추가해줘야 한다.
fp.writelines(['파일입출력', '테스트', '중입니다\n'])

# 파일 닫기
fp.close()

# 'newfile.txt' 파일을 추가 모드('a')로 열기
# 기존의 내용을 유지하고 새로운 내용을 추가할 수 있다.
fp = open('newfile.txt', 'a', encoding='UTF-8')

# write() : 추가로 문자열을 파일에 쓴다. 개행이 필요하면 직접 추가해야 한다.
fp.write('테스트 끝!\n')

# 파일 닫기
fp.close()
