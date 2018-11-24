def check_win(board):
    for i in range(1,10,3):
        if board[str(i)]==board[str(i+1)]==board[str(i+2)]:
           return True
    for i in range(1,4):
        if board[str(i)]==board[str(i+3)]==board[str(i+6)]:
            return True
    if board[str(1)]==board[str(5)]==board[str(9)]:
        return True
    if board[str(3)]==board[str(5)]==board[str(7)]:
        return True
def position_overload(board,position):
    if (board[position] == 'X' or board[position] == 'O'):
        return True
def check_blank_position(board):
    blank_positions = []
    for i in range(1,10):
        if (board[str(i)] == 'X' or board[str(i)] == 'O'):
            continue
        else:
            blank_positions += str(i)
    return blank_positions
def out_range(position):
    board = ['1','2','3','4','5','6','7','8','9']
    if position in board:
        return False
    else:
        return True
