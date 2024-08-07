# 논리 연산자 사용 예제
# 'and', 'or', 'not' 논리 연산자를 조합하여 다양한 결과를 출력

# 'and' 연산자는 두 값이 모두 True일 때만 True를 반환합니다.
print('False and False : ', False and False)  # 출력: False
print('False and True : ', False and True)   # 출력: False
print('True and False : ', True and False)    # 출력: False
print('True and True : ', True and True)      # 출력: True

# 'or' 연산자는 두 값 중 하나라도 True일 때 True를 반환합니다.
print('False or False : ', False or False)    # 출력: False
print('False or True : ', False or True)     # 출력: True
print('True or False : ', True or False)      # 출력: True
print('True or True : ', True or True)        # 출력: True

# 'not' 연산자는 논리 값을 반전시킵니다.
print('not False : ', not False)  # 출력: True
print('not True : ', not True)    # 출력: False
