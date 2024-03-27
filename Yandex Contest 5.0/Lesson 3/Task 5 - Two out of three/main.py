# Два из трех
#
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.
#
# Формат ввода
# Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины списка
# n (1 ≤ n ≤ 1000). Вторая строка описания содержит список натуральных чисел, записанных через пробел.
# Числа не превосходят 109.
#
# Формат вывода
# Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание,
# что каждое число необходимо выводить только один раз.
#
# Пример 1
# Ввод
# 2
# 3 1
# 2
# 1 3
# 2
# 1 2
#
# Вывод
# 1 3
#
# Пример 2
# Ввод
# 3
# 1 2 2
# 3
# 3 4 3
# 1
# 5
#
# Вывод
#


def main(nums1, nums2, nums3):
    res = set()
    first_ints = set(nums1).intersection(set(nums2))
    second_ints = set(nums2).intersection(set(nums3))
    third_ints = set(nums3).intersection(set(nums1))
    res = res.union(first_ints).union(second_ints).union(third_ints)

    return sorted(list(res))


with open('input.txt', 'r', encoding='utf-8') as file:
    count1 = int(file.readline())
    numbers1 = list(map(int, file.readline().split()))
    count2 = int(file.readline())
    numbers2 = list(map(int, file.readline().split()))
    count3 = int(file.readline())
    numbers3 = list(map(int, file.readline().split()))
ans = main(numbers1, numbers2, numbers3)
print(*ans)

# tests = [
#     ([3, 1], [1, 3], [1, 2], [1, 3]),
#     ([1, 2, 2], [3, 4, 3], [5], []),
#     ([1, 1, 1], [1, 1, 1], [1, 1, 1], [1]),
#     ([1], [2], [3], []),
#     ([3, 1], [4, 5], [1, 2], [1]),
#     ([1], [1], [1], [1]),
#     ([4, 4], [1, 2], [2, 3], [2]),
#     ([1, 2, 3], [4, 5, 6], [1, 5, 3], [1, 3, 5]),
# ]
# #
# for numbers1, numbers2, numbers3, ans in tests:
#     assert main(numbers1, numbers2, numbers3) == ans, f'Test {numbers1}, {numbers2}, {numbers3}, {ans}'
