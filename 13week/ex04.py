# 파일열기
# open(파일경로, 모드, encoding='UTF-8')
# 모드 r(read) : 읽기 / w(write) : 새로쓰기 / a(append) : 내용추가

# 같은 파일에 대해서...
# A 프로그램 : 읽는 중 (r)/ B 프로그램 : 읽을 수 있음 (r,w,a)
# A 프로그램 : 쓰는 중 (w,a)/ B 프로그램 : 읽을 수 없음 (r,w,a)
# A 프로그램 : 읽는 중 (r)/ B 프로그램 : 수정이 안됨 (w,a)

# 파일 읽기
# readline() : 한 줄 읽기
# readlines() : 모든 줄을 읽어서 리스트에 담아 반환
# 개행 문자도 읽어들이기 때문에 strip() 함수를 이용해서 자라내서 쓴다

# 파일 쓰기
# write(문자열) : 문자열을 파일에 쓴다
# writelines(문자열 리스트) : 리스트에 있는 문자열을 파일에 쓴다


# 파일 닫기
# close()
