import random


def get_number(a, b, text):
    while True:
        number_tab = int(input(text + f"in range of {a}-{b} :"))
        if a <= number_tab <= b:
            return number_tab
        else:
            print(f"Number must be in range of {a}-{b}!")


def ley_mines(n_rows, n_cols, n_mines):
    mines_set = set()
    while len(mines_set) < n_mines:
        n = random.randrange(n_rows)
        m = random.randrange(n_cols)
        mines_set.add((n, m))
    return mines_set


def number_of_neighboring_mines(field, mines_locations):
    count = 0
    i, j = field
    for m, n in [(i-1, j-1), (i-1, j), (i-1, j+1),
                 (i, j-1), (i, j+1),
                 (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if (m, n) in mines_locations:
            count += 1
    return count


def create_board(mines_locations, rows, columns):
    board = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if (i, j) in mines_locations:
                board[i].append(' *')
            else:
                n = number_of_neighboring_mines((i, j), mines_locations)
                board[i].append(n)
    return board


def reveal_fields(point, chosen, board):
    i, j = point
    if 0 < board[i][j] < 9:
        chosen.add((i, j))
    elif board[i][j] == 0:
        chosen.add((i, j))
        for m, n in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                     (i, j - 1), (i, j + 1),
                     (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
            if m in range(len(board)) and n in range(len(board[0])) and (m, n) not in chosen:
                reveal_fields((m, n), chosen, board)
    return chosen


def print_board(chosen, board):
    lista = [[] for _ in range(len(board))]
    cords_x = ["%2d" % i for i in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) in chosen and board[i][j] != " *":
                lista[i].append("%2d" % board[i][j])
            elif (i, j) in chosen and board[i][j] == " *":
                lista[i].append(board[i][j])
            else:
                lista[i].append('__')
    print(*cords_x, end="\n")
    for i in range(len(board)):
        print(*lista[i], end=f"  {i}\n")