def initialize_chess_board():
    board = [['Rb', 'Nb', 'Bb', 'Qb', 'Kb', 'Bb', 'Nb', 'Rb'],
             ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
             ['' for _ in range(8)],
             ['' for _ in range(8)],
             ['' for _ in range(8)],
             ['' for _ in range(8)],
             ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
             ['Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]
    return board

def read_moves_from_file(filename):
    moves = []
    with open(filename, 'r') as file:
        for line in file:
            moves.append(tuple(map(int, line.strip().split())))
    return moves

def write_captured_pieces_to_file(filename, pieces):
    with open(filename, 'w') as file:
        for piece in pieces:
            file.write(f"{piece}\n")

def main():
    board = initialize_chess_board()
    moves = read_moves_from_file('input.txt')
    captured_pieces = []

    for move in moves:
        from_col, from_row, to_col, to_row = move
        from_row, to_row = 7 - from_row, 7 - to_row

        if board[to_row][to_col]:
            captured_pieces.append(board[to_row][to_col])

        board[to_row][to_col] = board[from_row][from_col]
        board[from_row][from_col] = ''

    write_captured_pieces_to_file('output.txt', captured_pieces)

main()
