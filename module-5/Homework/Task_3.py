def is_valid(x, y, n, board):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1
def print_board(board):
    n = len(board)
    print("\n Маршрут коня:")
    for row in board:
        print(" ".join(f"{cell:2d}" for cell in row))
    print()
def generate_walk_knight(n, start_x, start_y):
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[start_x][start_y] = 0 
    def backtrack(x, y, move_num):
        if move_num == n * n - 1:
            return True
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            if is_valid(next_x, next_y, n, board):
                board[next_x][next_y] = move_num + 1
                if backtrack(next_x, next_y, move_num + 1):
                    return True
                board[next_x][next_y] = -1
        return False  
    if backtrack(start_x, start_y, 0):
        print_board(board)
        return True
    else:
        print("Ошибка.")
        return False
n = 6
print(f"Маршрут коня на доске {n}×{n}.")
print("Введите начальные координаты коня на доске(строка и столбец от 0 до {n-1}).")

try:
    start_x = int(input("Строка (0–5): "))
    start_y = int(input("Столбец (0–5: "))
    if not (0 <= start_x < n and 0 <= start_y < n):
        print("Ошибка: координаты вне доски.")
    else:
        generate_walk_knight(n, start_x, start_y)
except ValueError:
    print("Ошибка: введите целые числа.")
