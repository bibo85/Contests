# Плохой огородник
#
# Огород описывается матрицей N на M из неотрицательных чисел, обозначающих высоту сорняков в текущей клетке.
# Нужно выбрать строку и столбец, чтобы запущенность огорода стала как можно меньше.
# Вывод: строка и столбец

def find_max(w, bannedrow, bannedcol):
    answer = 0
    r = c = 0
    for i in range(len(w)):
        if i != bannedrow:
            for j in range(len(w[0])):
                if j != bannedcol and w[i][j] > answer:
                    answer = w[i][j]
                    r = i
                    c = j
    return r, c, answer


def find_max_row_and_col(n, m, weeds):
    # Находим абсолютный максимум
    find_row, find_col, max_val = find_max(weeds, -1, -1)

    # находим второй и третий максимумы, если сначала будем блокировать строку от абсолютного максимума
    bannedrowrow, bannedcol, tempval = find_max(weeds, find_row, -1)
    temp_row, temp_col, banrow_val = find_max(weeds, find_row, bannedcol)

    # находим второй и третий максимумы, если сначала будем блокировать столбец от абсолютного максимума
    bannedcolrow, bannedcolcol, tempval = find_max(weeds, -1, find_col)
    temp_row, temp_col, bancol_val = find_max(weeds, bannedcolrow, find_col)

    # сравнивая третий максимум проверяем какой из вариантов строк и столбцов наилучший
    if banrow_val > bancol_val:
        return [find_row + 1, bannedcol + 1]
    else:
        return [bannedcolrow + 1, find_col + 1]


# Test
tests = [
    (5, 3, [[4, 4, 1, 2], [3, 2, 1, 2], [0, 1, 2, 1], [2, 1, 9, 2], [4, 1, 0, 3]], [1, 3]),
]

for n, m, weeds, ans in tests:
    assert find_max_row_and_col(n, m, weeds) == ans, f'Test {n} {m} {weeds} {ans}'
