# Ограничение времени	2 секунды
# Ограничение памяти	256Mb
#
# Игра в крестики-нолики на бесконечной плоскости похожа на обычные крестики-нолики: два игрока по очереди ставят свои
# фигуры (крестики у первого игрока и нолики — у второго) в свободные клетки поля. Побеждает тот игрок, который первым
# выстроил пять своих фигур по горизонтали, вертикали или одной из диагоналей.
#
# В логе записаны координаты клеток, в том порядке, в котором игроки ставили свои фигуры. Определите, кто победил в
# игре или отследите ситуацию, что игроки увлеклись и продолжили игру после победы одного из игроков.
#
# Формат ввода
# В первой строке записано число n (1 ≤ n ≤ 10000) — количество ходов, которые совершили игроки.
#
# В следующих n строках записано по два числа r, c (|r|, |c| ≤ 109) — координаты клетки, в которую была поставлена
# очередная фигура. Гарантируется, что все координаты клеток уникальны (т.е. игрок не ставил свою фигуру в ту клетку,
# в которой уже стоит фигура)
#
# Формат вывода
# В случае победы первого игрока последним ходом выведите слово ”First”. В случае победы второго игрока последним
# ходом выведите слово ”Second”. Если ни один из игроков не успел победить выведите слово ”Draw”. Если ходы
# продолжились после победы одного из игроков выведите слово ”Inattention”.
#
# Пример 1
# Ввод
# 9
# 4 4
# 4 5
# 2 2
# 2 3
# 3 3
# 3 4
# 1 1
# 1 2
# 5 5
#
# Вывод
# First
#
# Пример 2
# Ввод
# 10
# 5 0
# 1 1
# 4 0
# 2 1
# 3 0
# 3 1
# 2 0
# 4 1
# 1 0
# 5 1
#
# Вывод
# Inattention


from typing import Dict, List


def check_winner(play_field: Dict[tuple, str], x: int, y: int, symbol: str) -> bool:
    # направления для проверки (горизонталь и вертикаль)
    directions: List[tuple[int, int]] = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dx, dy in directions:
        matches: int = 0
        # проверка в одном направлении
        for i in range(1, 5):
            new_direction_pos = (x + dx * i, y + dy * i)
            if new_direction_pos in play_field and play_field[new_direction_pos] == symbol:
                matches += 1
            else:
                break

        # проверка в противоположном направлении
        for i in range(1, 5):
            new_direction_neg = (x - dx * i, y - dy * i)
            if new_direction_neg in play_field and play_field[new_direction_neg] == symbol:
                matches += 1
            else:
                break

        if matches == 4:
            return True
    return False


def game() -> str:
    steps_cnt: int = int(input())
    steps: List[tuple[int, int]] = []
    for _ in range(steps_cnt):
        x, y = map(int, input().split())
        steps.append((x, y))

    play_field: Dict[tuple, str] = {}
    is_winner: bool = False
    winner: str = ""

    for idx, val in enumerate(steps):
        x, y = val
        sym: str = "x" if idx % 2 == 0 else "o"  # определяем какой символ ставить
        play_field[(x, y)] = sym  # заносим ход в словарь с ходами

        res = check_winner(play_field, x, y, sym)
        if res and not is_winner:
            is_winner = True
            winner = "First" if sym == "x" else "Second"
        elif is_winner:
            return "Inattention"
    return winner if winner else "Draw"


if __name__ == '__main__':
    ans: str = game()
    print(ans)
