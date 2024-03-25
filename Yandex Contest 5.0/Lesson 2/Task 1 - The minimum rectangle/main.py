# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами,
# параллельными линиям сетки, покрывающий все закрашенные клетки.
#
# Формат ввода
# Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100).
# На следующих K строках находятся пары чисел Xi и Yi — координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).
#
# Формат вывода
# Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.
#
# Пример
# Ввод
# 4
# 1 3
# 3 1
# 3 5
# 6 3
#
# Вывод
# 1 1 6 5


def get_coordinates(coors_):
    coor_left_corner = [float("inf"), float("inf")]
    coor_right_corner = [-float("inf"), -float("inf")]

    # Находим самые маленькие и самые большие координаты x и y
    for coor in coors_:
        if coor[0] < coor_left_corner[0]:
            coor_left_corner[0] = coor[0]
        if coor[1] < coor_left_corner[1]:
            coor_left_corner[1] = coor[1]
        if coor[0] > coor_right_corner[0]:
            coor_right_corner[0] = coor[0]
        if coor[1] > coor_right_corner[1]:
            coor_right_corner[1] = coor[1]
    coor_left_corner.extend(coor_right_corner)
    return " ".join(map(str, coor_left_corner))


with open('input.txt', 'r', encoding='utf-8') as file:
    coors_cnt = int(file.readline())
    coors = []
    for _ in range(coors_cnt):
        coors.append(list(map(int, file.readline().split())))
    ans = get_coordinates(coors)
    print(ans)

# Tests
# tests = [
#     (4, [[1, 3], [3, 1], [3, 5], [6, 3]], [1, 1, 6, 5]),
# ]
#
# for coor_cnt, i_coors, ans in tests:
#     assert get_coor(i_coors) == ans, f"Test {ans}"
