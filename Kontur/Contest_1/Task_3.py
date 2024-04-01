# Одержимый
#
# Ограничение по времени: 1 секунда
# Ограничение по памяти на тест: 256 мб
#
# Найти подотрезки массива. Интересный подотрезок - отрезов, в котором не более одного нуля и сумма всех элементов
# не более К.
#
# Вводные данные
# 1 строка: N и K, длина массива и максимальная сумма цифр в отрезке
# 2 строка: целые числа через пробел

def find_sub_sections(n, k, nums_lst):
    subs = []

    for i in range(n):
        j = i
        while j < n:
            sub_arr = nums_lst[i:j + 1]
            if sum(sub_arr) <= k and sub_arr.count(0) < 2:
                subs.append(sub_arr)
                j += 1
            else:
                break

    return len(subs)


# Test
tests = [
    ([4, 1], [0, 1, 1, 0], 6),
    ([4, 4], [1, 2, 3, 4], 5),
    ([11, 6], [1, 5, 2, 3, 0, 4, 0, 0, 3, 1, 2], 23),
]

for nk, nums, ans in tests:
    n = nk[0]
    k = nk[1]
    assert find_sub_sections(n, k, nums) == ans, f'Test {n} {k} {nums} {ans}'
