# Коллекционер
#
# Ограничение по времени: 1 секунда
# Ограничение по памяти на тест: 256 мб
#
# Найти максимальную площадь возможного прямоугольника по координатам


def is_rectangle(point1, point2, point3, point4):
    return point1[0] == point2[0] and point1[1] == point4[1] and point2[1] == point3[1] and point3[0] == point4[0]


def find_max_area(cnt, coors_lst):
    max_area = 0
    for i1 in range(cnt):
        for i3 in range(cnt):
            coor_2 = [coors_lst[i1][0], coors_lst[i3][1]]
            coor_4 = [coors_lst[i3][0], coors_lst[i1][1]]
            if coor_2 in coors_lst and coor_4 in coors_lst:
                area = abs(coors_lst[i1][0] - coor_4[0]) * abs(coors_lst[i1][1] - coor_2[1])
                if area > max_area:
                    result = is_rectangle(coors_lst[i1], coor_2, coors_lst[i3], coor_4)
                    if result:
                        max_area = area

    return max_area


with open('../../input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, file.readline().split())))
    ans = find_max_area(n, nums)
    print(ans)

# Test
# tests = [
#     (8, [[0, 0], [1, 1], [0, 2], [5, 0], [5, 2], [0, 4], [3, 0], [3, 4]], 12),
#     (4, [[1, -1], [1, 1], [-1, 1], [1, 0]], 0)
# ]
#
# for n, coors, ans in tests:
#     assert find_max_area(n, coors) == ans
