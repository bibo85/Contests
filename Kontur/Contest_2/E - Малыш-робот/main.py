# Прошел 25 тестов
# 8 баллов получено
# применение авторской методики дает "Отказ тестирования"


def check_intersection(key, start_p, end_p, points):
    if key not in points:
        return False
    if start_p > end_p:
        start_p, end_p = end_p, start_p

    return {num for num in range(start_p, end_p + 1)} & points[key]


def get_input():
    inpt_data = input().split()
    return inpt_data[0], int(inpt_data[1])


def get_input_coordinates():
    inpt_coors = input().split()
    return int(inpt_coors[0]), int(inpt_coors[1])


points_cnt = int(input())  # количество препятствий
dx = {"U": 0, "D": 0, "R": 1, "L": -1}
dy = {"U": 1, "D": -1, "R": 0, "L": 0}

# Создаем словари координат препятствий
points_x = {}  # координаты препятствий по x
points_y = {}  # координаты препятствий по y
for i in range(points_cnt):
    x, y = get_input_coordinates()
    if x not in points_x:
        points_x[x] = set()
    points_x[x].add(y)
    if y not in points_y:
        points_y[y] = set()
    points_y[y].add(x)

n = int(input())
cur_x = 0
cur_y = 0
is_intersection = 0
for i in range(1, n + 1):
    cur_direction, dist = get_input()
    if cur_direction in ("U", "D"):
        ny = cur_y + dy[cur_direction] * dist
        nx = cur_x
    else:
        nx = cur_x + dx[cur_direction] * dist
        ny = cur_y

    if cur_x == nx:
        is_intersection = check_intersection(cur_y, cur_y, ny, points_x)
    elif cur_y == ny:
        is_intersection = check_intersection(cur_x, cur_x, nx, points_y)

    if is_intersection:
        print("Stop", i)
        exit()

    cur_x = nx
    cur_y = ny

print("Complete")
