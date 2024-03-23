# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Вам дана последовательность измерений некоторой величины.
# Требуется определить, повторялась ли какое-либо число, причём расстояние между повторами не превосходило k.
#
# Формат ввода
# В первой строке задаются два числа n и k (1 ≤ n, k ≤ 105).
#
# Во второй строке задаются n чисел, по модулю не превосходящих 109.
#
# Формат вывода
# Выведите YES, если найдется повторяющееся число и расстояние между повторами не превосходит k и NO в противном случае.
#
# Пример 1
# Ввод
# 4 2
# 1 2 3 1
#
# Вывод
# NO
#
# Пример 2
# Ввод
# 4 1
# 1 0 1 1
#
# Вывод
# YES
#
# Пример 3
# Ввод
# 6 2
# 1 2 3 1 2 3
#
# Вывод
# NO


def repeat_check(n_k, nums):
    num_dict = {}
    for i in range(n_k[0]):
        if nums[i] in num_dict and abs(i - num_dict[nums[i]]) <= n_k[1]:
            return "YES"
        else:
            num_dict[nums[i]] = i
    return "NO"


with open('input.txt', 'r', encoding='utf-8') as file:
    nk = list(map(int, file.readline().split()))
    numbers = list(map(int, file.readline().split()))
    ans = repeat_check(nk, numbers)
    print(ans)

# Tests
# tests = [
#     ([4, 2], [1, 2, 3, 1], "NO"),
#     ([4, 1], [1, 0, 1, 1], "YES")
# ]
#
# for nk, i_nums, ans in tests:
#     assert repeat_check(nk, i_nums) == ans, f'Test {nk}, {i_nums}, {ans}'
