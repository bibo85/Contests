# Ограничение времени	2 секунды
# Ограничение памяти	256Mb
#
# Дан массив целых положительных чисел a длины n. Разбейте его на минимально возможное количество отрезков,
# чтобы каждое число было не меньше длины отрезка которому оно принадлежит.
# Длиной отрезка считается количество чисел в нем.
#
# Разбиение массива на отрезки считается корректным, если каждый элемент принадлежит ровно одному отрезку.
#
# Формат ввода
# Первая строка содержит одно целое число t (1 ≤ t ≤ 1000) — количество наборов тестовых данных.
# Затем следуют t наборов тестовых данных.
#
# Первая строка набора тестовых данных содержит одно целое число n (1 ≤ n ≤ 105) — длину массива.
#
# Следующая строка содержит n целых чисел a1, a2, …, an (1 ≤ ai ≤ n) — массив a.
#
# Гарантируется, что сумма n по всем наборам тестовых данных не превосходит 2 ⋅ 105.
#
# Формат вывода
# Для каждого набора тестовых данных в первой строке выведите число k — количество отрезков в вашем разбиении.
#
# Затем в следующей строке выведите k чисел len1, len2, …, lenk  — длины отрезков в порядке слева направо.
#
# Пример
# Ввод
# 3
# 5
# 1 3 3 3 2
# 16
# 1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9
# 7
# 7 2 3 4 3 2 7
#
# Вывод
# 3
# 1 2 2
# 3
# 1 6 9
# 3
# 2 3 2

def get_segments(length, numbers):
    if len(numbers) < 2:
        return [numbers]
    res = []
    cur_lst = [numbers[0]]
    max_length = numbers[0]
    for i in range(1, length - 1):
        if max_length > len(cur_lst) and len(cur_lst) + 1 <= numbers[i]:
            cur_lst.append(numbers[i])
            max_length = min(max_length, numbers[i])
        else:
            res.append(cur_lst)
            cur_lst = [numbers[i]]
            max_length = numbers[i]

    max_length = min(max_length, numbers[-1])
    if max_length > len(cur_lst):
        cur_lst.append(numbers[-1])
        res.append(cur_lst)
    else:
        res.append(cur_lst)
        res.append([numbers[-1]])

    return res


with open('input.txt', 'r', encoding='utf-8') as file:
    count_segments = int(file.readline())
    res_str = ""
    for _ in range(count_segments):
        length_segment = int(file.readline())
        num_list = list(map(int, file.readline().split()))
        result = get_segments(length_segment, num_list)

        res_str += str(len(result)) + "\n"
        for i_res in result:
            res_str += str(len(i_res)) + " "
        res_str += "\n"
    print(res_str.strip())
