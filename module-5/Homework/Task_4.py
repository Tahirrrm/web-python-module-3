import random
def print_board(board):
    print("\n" + "-" * 20)
    for i in range(4):
        row = board[i*4:(i+1)*4]
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("   |", end="")
            else:
                print(f"{cell:2} |", end="")
        print("\n" + "-" * 20)
def check_win(board):
    return board == list(range(1, 16)) + [0]
def get_zero_index(board):
    return board.index(0)
def can_move(zero_index, direction):
    row, col = zero_index // 4, zero_index % 4
    if direction == 'w' and row > 0:  return True
    if direction == 's' and row < 3:  return True
    if direction == 'a' and col > 0:  return True
    if direction == 'd' and col < 3:  return True
    return False
def make_move(board, zero_index, direction):
    row, col = zero_index // 4, zero_index % 4
    if direction == 'w': target = (row - 1) * 4 + col
    elif direction == 's': target = (row + 1) * 4 + col
    elif direction == 'a': target = row * 4 + (col - 1)
    elif direction == 'd': target = row * 4 + (col + 1)
    board[zero_index], board[target] = board[target], board[zero_index]
def game_loop(board):
    print_board(board)
    if check_win(board):
        print("\n Победа! ")
        return 
    move = input("Ваш ход (w/a/s/d/q): ").strip().lower() 
    if move == 'q':
        print("Игра окончена.")
        return  
    if move not in ['w', 'a', 's', 'd']:
        print("Используйте w, a, s, d или q.")
        return game_loop(board) 
    zero_index = get_zero_index(board)
    if can_move(zero_index, move):
        make_move(board, zero_index, move)
    else:
        print("Нельзя пойти в этом направлении.")
    game_loop(board)
board = list(range(1, 16)) + [0]
random.shuffle(board)
print("Пятнашки")
print("Управление: w — вверх, s — вниз, a — влево, d — вправо. q — выход.")
game_loop(board)  