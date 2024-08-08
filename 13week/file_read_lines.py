# 'myfile.txt' 파일을 UTF-8 인코딩 방식으로 읽기
fp = open('myfile.txt', 'r', encoding='UTF-8')

# readlines()로 파일의 모든 줄을 읽어 리스트로 반환
# 각 줄의 양쪽 공백을 제거하기 위해 strip() 사용
lines = [x.strip() for x in fp.readlines()]

# 리스트 전체를 출력
print(lines)

# 리스트의 각 줄을 인덱스와 함께 출력
# enumerate()를 사용하여 각 줄과 인덱스를 가져옴
for idx, line in enumerate(lines):
    print(f'{idx+1} : {line}')

# 파일 닫기
fp.close()
