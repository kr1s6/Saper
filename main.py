import minesweeper as mst


def count_all(list_e):
    count = 0
    for element in list_e:
        count += len(element)
    return count


def sapper():
    rows = mst.get_number(8, 30, "Give amount of rows ")
    columns = mst.get_number(8, 24, "Give amount of columns ")

    mines_max_amount = int(rows * columns / 3)
    mines = mst.get_number(0, mines_max_amount, "Give amount of mines ")

    mines_locations = mst.ley_mines(rows, columns, mines)
    board = mst.create_board(mines_locations, rows, columns)

    lista = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for _ in range(len(board[0])):
            lista[i].append("__")

    cords_x = ["%2d" % i for i in range(len(board[0]))]
    print(*cords_x, end="\n")
    for i in range(rows):
        print(*lista[i], end=f"  {i}\n")

    chosen = set()
    while len(chosen) != (count_all(board) - mines):
        i, j = map(int, input("Chose field: enter two numbers (row, column): ").split())

        if (i, j) in mines_locations:
            chosen.update(mines_locations)
            # chosen.add((i, j))
            print(5*"_" + "GAME OVER" + 5*"_")
            mst.print_board(chosen, board)
            print(5 * "_" + "GAME OVER" + 5 * "_")
            break
        else:
            chosen.add((i, j))
            chosen.update(mst.reveal_fields((i, j), chosen, board))
            mst.print_board(chosen, board)

    if len(chosen) == (count_all(board) - mines):
        print(5*"_" + "Congratulation, you finished the game!" + 5*"_")
        mst.print_board(chosen, board)


if __name__ == "__main__":
    sapper()