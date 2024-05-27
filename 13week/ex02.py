
fp = open('myfile.txt', 'r', encoding='UTF-8')

# readlines() : 파일의 각 줄을 리스트에 담아 반환
lines = [x.strip() for x in fp.readlines()]
print(lines)
for idx, line in enumerate(lines):
    print(f'{idx+1} : {line}')

fp.close()