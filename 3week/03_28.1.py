# for 변수 in 순서가 있는 데이터
# 순서가 있는 데이터를 하나씩 가져와 변수에 대입하여 사용

# 예시 1. 기본형
for n in [1, 2, 3]:
    print(n)

# 예시 2. 순서가 있는 데이터의 변경
for n in [54, -12, '안녕', 4.5]:
    print(n)

# 예시 3. 변수명도 자유
for std_no in [123, 723, 711, 552]:
    print(std_no)

# 반복횟수를 직접 결정하고 싶다면?
# 반복횟수는 순서가 있는 데이터의 갯수에 따라 결정됨
# 원하는 횟수만큼 반복시키려면 그 갯수만큼의 데이터를 전달하면 됨

# 파이썬 기본 문법 중에 가장 적절한 데이터형 range 객체 !
# range 객체 : 수열을 만드는 객체
# range(끝값)     => 0 부터 끝값-1 까지의 수열을 생성
# range(시작값,끝값) => 시작값부터 끝값-1까지의 수열을 생성
# range(시작값,끝값,증감값) => 시작값부터 증감값을 계속반영하면서
#                           끝값을 넘어서지 않는 범위의 수열을 생성

# range는 for문에 종속된 문법이 xxx
for n in range(5):
    print('안녕')

# 파이썬에서 for문의 사용 방식
# 1. 순서가 있는 데이터에서 하나씩 값을 가져와서 사용
mystr = 'AABCADF'
a_count = 0
for c in mystr:
    if c == 'A':
        a_count += 1
        print(f'{mystr}에서 A는 {a_count}개 ')

for _ in range(5):  # 언더바 : 와일드카드 -> 값을 버림
    print("")

for i in range(5):
    print(i, end='>> ')
