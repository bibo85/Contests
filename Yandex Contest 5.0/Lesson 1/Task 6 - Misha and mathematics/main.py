# Миша и математика
#
# Ограничение времени	1 секунда
# Ограничение памяти	256Mb
#
# Миша сидел на занятиях математики в Высшей школе экономики и решал следующую задачу: дано n целых чисел и нужно
# расставить между ними знаки + и × так, чтобы результат полученного арифметического выражения был нечётным
# (например, между числами 5, 7, 2, можно расставить арифметические знаки следующим образом: 5×7+2=37).
# Так как примеры становились все больше и больше, а Миша срочно убегает в гости, от вас требуется написать
# программу решающую данную задачу.
#
# Формат ввода
# В первой строке содержится единственное число n (2≤n≤10**5). Во второй строке содержится n целых чисел a(i),
# разделённых пробелами (−10**9≤a(i)≤10**9). Гарантируется, что решение существует.
#
# Формат вывода
# В одной строке выведите n−1 символ + или ×, в результате применения которых получается нечётный результат.
# (Для вывода используйте соответственно знаки «+» (ASCII код—43) и «x» (ASCII код—120), без кавычек).
#
# Пример 1
# Ввод
# 3
# 5 7 2
#
# Вывод
# x+
#
# Пример 2
# Ввод
# 2
# 4 -5
#
# Вывод
# +

with open('input.txt', 'r', encoding='utf-8') as file:
    cnt = int(file.readline())
    nums = list(map(int, file.readline().split()))
    ans = ''
    is_even = True if nums[0] % 2 == 0 else False

    for i in range(1, cnt):
        if not is_even and nums[i] % 2 != 0:
            ans = ''.join([ans, chr(120)])
            is_even = False
        elif is_even and nums[i] % 2 == 0:
            ans = ''.join([ans, chr(43)])
            is_even = True
        else:
            ans = ''.join([ans, chr(43)])
            is_even = False

    print(ans)
