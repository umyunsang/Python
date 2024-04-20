# 가위,바위,보 프로그램

import random

me = '999'
while me != '1':
    me = input('가위/바위/보 중에 입력 : ')
    com = random.choice(['가위', '바위', '보'])

    print(f'나의 선택 : {me}')
    print(f'컴퓨터의 선택 : {com}')

    if me == com:
        print("비김")
    elif me == '가위':
        if com == '보':
            print('이김')
        else:
            print('짐')
    elif me == '바위':
        if com == '가위':
            print('이김')
        else:
            print('짐')
    elif me == '보':
        if com == '바위':
            print('이김')
        else:
            print('짐')
    else:
        print("잘못입력")
