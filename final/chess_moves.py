def initialize_chess_board():
    # 체스 보드를 초기화하는 함수
    # 흑백 체스말과 빈칸으로 이루어진 8x8 보드 생성
    board = [['Rb', 'Nb', 'Bb', 'Qb', 'Kb', 'Bb', 'Nb', 'Rb'],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['' for _ in range(8)],  # 빈 칸
             ['' for _ in range(8)],  # 빈 칸
             ['' for _ in range(8)],  # 빈 칸
             ['' for _ in range(8)],  # 빈 칸
             ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
             ['Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]
    return board

def read_moves_from_file(filename):
    # 파일에서 이동 정보를 읽어오는 함수
    # 파일의 각 줄을 읽고, 각 줄의 이동 정보를 튜플로 변환하여 리스트에 저장
    moves = []
    with open(filename, 'r') as file:
        for line in file:
            moves.append(tuple(map(int, line.strip().split())))
    return moves

def write_captured_pieces_to_file(filename, pieces):
    # 캡처된 체스말을 파일에 기록하는 함수
    with open(filename, 'w') as file:
        for piece in pieces:
            file.write(f"{piece}\n")

def main():
    # 체스 보드 초기화
    board = initialize_chess_board()
    # 파일에서 이동 정보를 읽어옴
    moves = read_moves_from_file('input.txt')
    captured_pieces = []

    # 이동 처리
    for move in moves:
        from_col, from_row, to_col, to_row = move
        from_row, to_row = 7 - from_row, 7 - to_row  # 좌표 변환

        # 이동할 위치에 말이 있다면 캡처된 말 목록에 추가
        if board[to_row][to_col]:
            captured_pieces.append(board[to_row][to_col])

        # 말 이동 처리
        board[to_row][to_col] = board[from_row][from_col]
        board[from_row][from_col] = ''

    # 캡처된 말 목록을 파일에 기록
    write_captured_pieces_to_file('output.txt', captured_pieces)

# 프로그램 실행
main()
