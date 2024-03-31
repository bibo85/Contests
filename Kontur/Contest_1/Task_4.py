# Общительный человек

# Ограничение по времени: 2  секунда
# Ограничение по памяти на тест: 256 мб
#
# Друзья одновременно бросают по кубику. Числа, выпавшие на гранях кубика, в сумме дают случайное число.
# Вычислисть, сколько случайних чисел может получиться по итогу.
#
# Первая строка: количество друзей
# Последующие строки: числа записанные на гранях кубика
#
# Пример
# Вход
# 3
# 0 1 2 3 4 5
# 0 0 2 3 4 5
# 3 4 5 0 0 0
#
# Выход
# 16

from itertools import combinations


def count_combinations(n, nums):
    lst = []
    for num in nums:
        lst.extend(num)
    comb_set = set(map(sum, combinations(lst, n)))
    return len(comb_set)


tests = [
    (3, [[0, 1, 2, 3, 4, 5], [0, 0, 2, 3, 4, 5], [3, 4, 5, 0, 0, 0]], 16),
]

for n, nums, ans in tests:
    assert count_combinations(n, nums) == ans, f'Test {n} {nums} {ans}'
