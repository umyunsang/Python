fp = open('newfile.txt', 'w', encoding='UTF-8')

# write(문자열) : 문자열을 파일에 쓴다
# writelines(문자열 리스트) : 리스트에 있는 문자열을 파일에 쓴다
# 둘 다 자동으로 개행해주지 않는다.
fp.write('안녕')
fp.write('하세요\n')
fp.writelines(['파일입출력','테스트','중입니다\n'])

fp.close()

fp = open('newfile.txt', 'a', encoding='UTF-8')
fp.write('테스트 끝!\n')
fp.close()
