'''
N x N 크기의 정사각형 행렬 형태의 리스트가 있습니다.
이 행렬의 왼쪽 상단부터 오른쪽 하단으로의 대각선 숫자의 합과
왼쪽 하단부터 오른쪽 상단으로의 대각선 숫자의 합을 구해 출력하는 코드를 작성하세요.
'''

# [심화] -100 ~ 100 임의의 값을 받고 리스트도 N x N input 받고
list_input = [[11, -2, 4],
              [4, 5, 6],
              [10, -12, 9]]
hap_up,hap_down = 0,0
for i in range(len(list_input)):
    hap_up += list_input[i][i]

for i in range(len(list_input)):
    hap_down += list_input[i][-i-1]
    # += list_input[len(list_input)-1-i][i]

print(f'주대각선의 합 : {hap_up}')
print(f'부대각선의 합 : {hap_down}')