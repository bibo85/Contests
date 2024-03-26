# Удаление чисел
#
# Ограничение времени	1 секунда
# Ограничение памяти	256Mb
#
# Дан массив a из n чисел. Найдите минимальное количество чисел, после удаления которых попарная разность оставшихся
# чисел по модулю не будет превышать 1, то есть после удаления ни одно число не должно отличаться от какого-либо
# другого более чем на 1.
#
# Формат ввода
# Первая строка содержит одно целое число n (1 ≤ n ≤ 2*10**5) — количество элементов массива a.
# Вторая строка содержит n целых чисел a(1), a(2),…,a(n) (0 ≤ a(i) ≤ 10**5) — элементы массива a.

# Формат вывода
# Выведите одно число — ответ на задачу.


def main(num_cnt, numbers):
    unic = set(numbers)
    if len(unic) < 2:
        return 0
    nums_map = {}
    for i in range(num_cnt):
        nums_map[numbers[i]] = nums_map.get(numbers[i], 0) + 1

    unic_list = sorted(list(unic))
    maximum = 0
    for i in range(len(unic_list) - 1):
        if unic_list[i + 1] - unic_list[i] <= 1:
            maximum = max(maximum, (nums_map[unic_list[i + 1]] + nums_map[unic_list[i]]))

    if maximum == num_cnt:
        return 0
    elif not maximum:
        return num_cnt - 1
    else:
        return num_cnt - maximum


with open('input.txt', 'r', encoding='utf-8') as file:
    num_cnt = int(file.readline())
    numbers = list(map(int, file.readline().split()))
ans = main(num_cnt, numbers)
print(ans)

# tests = [
#     (5, [1, 2, 3, 4, 5], 3),
#     (10, [1, 1, 2, 3, 5, 5, 2, 2, 1, 5], 4),
#     (5, [1, 3, 5, 7, 9], 4),
#     (1, [1], 0),
#     (10, [22238, 38788, 73611, 22861, 18865, 52721, 85325, 98901, 72035, 74803], 9),
#     (10, [26635, 26635, 26635, 26635, 26634, 26634, 26634, 26634, 26635, 26634], 0),
#     (1, [33292], 0),
#     (10, [22238, 22238, 22238, 22238, 22238, 22238, 22238, 22238, 22238, 22238], 0)
# ]
#
# for num_cnt, numbers, ans in tests:
#     assert main(num_cnt, numbers) == ans, f'Test {num_cnt}, {numbers}, {ans}'
