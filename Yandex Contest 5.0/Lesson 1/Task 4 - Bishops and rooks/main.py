# Слоны и ладьи
#
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# На шахматной доске стоят слоны и ладьи, необходимо посчитать, сколько клеток не бьется ни одной из фигур.
#
# Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали и вертикали, проходящих через клетку,
# где она стоит, до первой встретившейся фигуры. Слон бьет все клетки обеих диагоналей, проходящих через клетку,
# где он стоит, до первой встретившейся фигуры.
#
# Формат ввода
# В первых восьми строках ввода описывается шахматная доска. Первые восемь символов каждой из этих строк описывают
# состояние соответствующей горизонтали: символ B (заглавная латинская буква) означает, что в клетке стоит слон,
# символ R — ладья, символ * — что клетка пуста. После описания горизонтали в строке могут идти пробелы, однако
# длина каждой строки не превышает 250 символов. После описания доски в файле могут быть пустые строки.
#
# Формат вывода
# Выведите количество пустых клеток, которые не бьются ни одной из фигур.
#
# Пример 1
# Ввод
# ********
# ********
# *R******
# ********
# ********
# ********
# ********
# ********
#
# Вывод
# 49
#
# Пример 2
# Ввод	Вывод
# ********
# ********
# ******B*
# ********
# ********
# ********
# ********
# ********
#
# Вывод
# 54
#
# Пример 3
# Ввод
# ********
# *R******
# ********
# *****B**
# ********
# ********
# ********
# ********
#
# Вывод
# 40


def rook(chessboard, x, y):
    for i in range(1, 8):
        try:
            if chessboard[x + i][y] != "F":
                chessboard[x + i][y] = "."
            else:
                break
        except IndexError:
            break

    for i in range(1, 8):
        try:
            if chessboard[x][y + i] != "F":
                chessboard[x][y + i] = "."
            else:
                break
        except IndexError:
            break

    for i in range(1, 8):
        try:
            if chessboard[x - i][y] != "F" and x - i > -1:
                chessboard[x - i][y] = "."
            else:
                break
        except IndexError:
            break

    for i in range(1, 8):
        try:
            if chessboard[x][y - i] != "F" and y - i > -1:
                chessboard[x][y - i] = "."
            else:
                break
        except IndexError:
            break

    return chessboard


def bishop(chessboard, x, y):
    for i in range(1, 9):
        try:
            if x - i > -1 and y - i > -1 and chessboard[x - i][y - i] != "F":
                chessboard[x - i][y - i] = "."
            else:
                break
        except IndexError:
            break

    for i in range(1, 9):
        try:
            if x - i > -1 and chessboard[x - i][y + i] != "F":
                chessboard[x - i][y + i] = "."
            else:
                break
        except IndexError:
            break

    for i in range(1, 9):
        try:
            if y - i > -1 and chessboard[x + i][y - i] != "F":
                chessboard[x + i][y - i] = "."
            else:
                break
        except IndexError:
            break

    for i in range(1, 9):
        try:
            if chessboard[x + i][y + i] != "F":
                chessboard[x + i][y + i] = "."
            else:
                break
        except IndexError:
            break

    return chessboard


with open('input.txt', 'r', encoding='utf-8') as file:
    board = [file.readline() for i in range(1, 9)]
    chess_board = []
    for line in board:
        line = list(line.rstrip())
        if len(line) < 8:
            line.extend(["*"] * (8 - len(line)))
        chess_board.append(line)

    rooks = []  # ладьи
    bishops = []  # слоны
    result = 0

    for i in range(8):
        for n in range(8):
            try:
                j = chess_board[i].index("R")
                rooks.append([i, j])
                chess_board[i][j] = "F"
            except ValueError:
                break

    for i in range(8):
        for _ in range(8):
            try:
                j = chess_board[i].index("B")
                bishops.append([i, j])
                chess_board[i][j] = "F"
            except ValueError:
                break

    for i in rooks:
        chess_board = rook(chess_board, i[0], i[1])
    for i in bishops:
        chess_board = bishop(chess_board, i[0], i[1])

    for i in chess_board:
        result += i.count("*")

    print(result)
