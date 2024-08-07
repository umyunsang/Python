# 자료형 개요
# int : 정수형 / float : 실수형 / str : 문자형 / bool : 논리형

# C언어에서 변수 선언할 때 자료형도 함께 선언
# 예) int var1 = 100;

# 파이썬은 변수를 선언할 때 자료형 선언을 하지 않음

# escape character
# 다음에 오는 문자가 문법적 해석에서 탈출한다.
# 예) "안녕!" 이라는 문자열 출력
print("\"안녕!\"")
print("문자열에서 개행문자를 넣고 싶을 땐 \\n을 쓰면 됩니다!")

# 표현하려는 문장에 큰따옴표가 있으면 문자열을 작은 따옴표로 감싸면 됨
print('"안녕~~!"')
print("'(생각중)'")

# 큰따옴표와 작은따옴표가 둘 다 있으면...
print(''' "안녕!!!" '반갑습니다' ''')

# len() 함수: 문자열의 글자 수 세기, 파이썬 내장함수
msg = 'abcde'
print(len(msg))  # 출력: 5

# upper() 메서드: 소문자를 대문자로 변환
# isupper() 메서드: 문자열이 모두 대문자인지 확인하여 결과를 True/False로 반환
print(msg.upper())  # 출력: ABCDE
print(msg.upper().isupper())  # 출력: True

# lower() 메서드: 대문자를 소문자로 변환
# islower() 메서드: 문자열이 모두 소문자인지 확인하여 결과를 True/False로 반환
print(msg.upper().lower())  # 출력: abcde
print(msg.islower())  # 출력: True

# count() 메서드: 문자열에서 특정 문자가 몇 번 나왔는지 확인
print(msg.count('a'))  # 출력: 1

# find() 메서드: 특정 문자가 문자열의 몇 번째에 위치하는지 찾음 (문자열의 0번째부터 시작)
print(msg.find('c'))  # 출력: 2

# 인덱싱 (Indexing): 순서가 있는 데이터에 대해 순번으로 값을 가져오는 것
# 순번(index)은 0부터 시작
# 0 ~ len() - 1 까지의 인덱스가 있음
print(msg[2])  # 출력: c
print(msg[4])  # 출력: e

# 문자열 슬라이싱 (Slicing): 부분 문자열을 가져오는 것
# 문자열[start:end] 형태로 사용, start 인덱스부터 end 인덱스 전까지의 문자열을 반환
print(msg[1:4])  # 출력: bcd

# 문자열 연결 (Concatenation): 두 개 이상의 문자열을 연결
msg2 = "fghij"
print(msg + msg2)  # 출력: abcdefghij

# 문자열 반복 (Repetition): 문자열을 여러 번 반복
print(msg * 3)  # 출력: abcdeabcdeabcde
