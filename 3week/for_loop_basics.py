# for 변수 in 순서가 있는 데이터
# 순서가 있는 데이터를 하나씩 가져와 변수에 대입하여 사용

# 예시 1. 기본형
print("예시 1: 기본형")
for n in [1, 2, 3]:
    print(n)

# 예시 2. 다양한 데이터형을 포함하는 리스트
print("\n예시 2: 순서가 있는 데이터의 변경")
for n in [54, -12, '안녕', 4.5]:
    print(n)

# 예시 3. 변수명 자유롭게 설정
print("\n예시 3: 변수명도 자유")
for std_no in [123, 723, 711, 552]:
    print(std_no)

# 반복횟수를 직접 결정하고 싶다면?
# range 객체를 사용하여 반복 횟수를 결정할 수 있음

# range 객체 : 수열을 만드는 객체
# range(끝값)     => 0 부터 끝값-1 까지의 수열을 생성
# range(시작값,끝값) => 시작값부터 끝값-1까지의 수열을 생성
# range(시작값,끝값,증감값) => 시작값부터 증감값을 계속 반영하면서 끝값을 넘어서지 않는 범위의 수열을 생성

# range는 for문에 종속된 문법
print("\nrange를 사용한 반복")
for n in range(5):
    print('안녕')

# 문자열에서 특정 문자의 개수를 세는 예제
print("\n문자열에서 특정 문자 개수 세기")
mystr = 'AABCADF'
a_count = 0
for c in mystr:
    if c == 'A':
        a_count += 1
print(f'{mystr}에서 A는 {a_count}개')

# _ (언더바) : 값을 버림, 주로 반복 변수로 사용하지 않을 때
print("\n언더바를 사용한 반복")
for _ in range(5):  # 언더바는 값에 관심이 없음을 의미
    print("")

# 인덱스와 값을 함께 출력하는 예제
print("\n인덱스와 값을 함께 출력")
for i in range(5):
    print(i, end='>> ')
