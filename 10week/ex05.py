# 지역변수와 전역변수
# local variable and global variable

# 부모와 자식(종속)을 구분하는 기준
# => 들여쓰기 수준(indentation level)

# 전역(global) : 들여쓰기가 없는 코드(들여쓰기 수준이 0)
a = 100
if a == 100:
    print(a)

# 자식코드는 부모코드에서 사용되는 정보를 알 수 있다
# 부모코드는 자식코드에서 사용되는 정보를 알 수 없다
# 함수는 자식코드로 간주함
