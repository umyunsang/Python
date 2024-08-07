# 랜덤 숫자 뽑기 프로그램

# random 모듈을 사용하기 위해 임포트
import random

# 1부터 45까지의 숫자 중 하나를 무작위로 선택
num = random.randint(1, 45)

# 선택된 숫자를 출력
print(f'랜덤으로 선택된 숫자: {num}')

# 추가 내용: 여러 개의 랜덤 숫자 뽑기
# 1부터 45까지의 숫자 중 6개의 숫자를 무작위로 선택
random_numbers = random.sample(range(1, 46), 6)

# 선택된 숫자들을 정렬하여 출력
print(f'랜덤으로 선택된 6개의 숫자: {sorted(random_numbers)}')

# 추가 내용: 특정 범위 내에서의 난수 생성
# 1.0부터 10.0 사이의 실수를 무작위로 생성
random_float = random.uniform(1.0, 10.0)
print(f'랜덤으로 선택된 실수: {random_float:.2f}')
