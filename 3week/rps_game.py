# 가위, 바위, 보 게임 프로그램

import random  # 랜덤 모듈을 임포트하여 컴퓨터의 선택을 랜덤으로 결정함

me = '999'  # 사용자 입력의 초기값 설정

# 사용자가 '1'을 입력할 때까지 반복
while me != '1':
    # 사용자로부터 '가위', '바위', '보' 중 하나를 입력받음
    me = input('가위/바위/보 중에 입력 (종료하려면 1 입력) : ')

    # 컴퓨터의 선택을 랜덤으로 결정
    com = random.choice(['가위', '바위', '보'])

    # 사용자와 컴퓨터의 선택을 출력
    print(f'나의 선택 : {me}')
    print(f'컴퓨터의 선택 : {com}')

    # 게임 결과를 결정하여 출력
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
    elif me == '1':
        print("게임을 종료합니다.")
    else:
        # 잘못된 입력 처리
        print("잘못된 입력입니다. '가위', '바위', '보' 중에서 입력해주세요.")

# 추가: 게임 종료 후 최종 메시지
print("게임이 종료되었습니다.")
