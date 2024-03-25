# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Задано две строки, нужно проверить, является ли одна анаграммой другой.
# Анаграммой называется строка, полученная из другой перестановкой букв.
#
# Формат ввода
# Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.
#
# Формат вывода
# Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.
#
# Пример 1
# Ввод
# dusty
# study
#
# Вывод
# YES
#
# Пример 2
# Ввод
# rat
# bat
#
# Вывод
# NO
#
#
# Можно решить в 3 строчки
#
# from collections import Counter
#
# def is_anagram(str1, str2):
#     res = "YES" if Counter(str1) == Counter(str2) else "NO"
#     return res


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return "None"

    str1_dict = {}
    for el in str1:
        str1_dict[el] = str1_dict.get(el, 0) + 1

    str2_dict = {}
    for el in str2:
        str2_dict[el] = str2_dict.get(el, 0) + 1

    for key in str1_dict:
        num1 = str1_dict.get(key, 0)
        num2 = str2_dict.get(key, 0)
        if num1 != num2:
            return "NO"

    return "YES"


with open('input.txt', 'r', encoding='utf-8') as file:
    string1 = file.readline()
    string2 = file.readline()
    ans = is_anagram(string1, string2)
    print(ans)

# Tests
tests = [
    ("dusty", "study", "YES"),
    ("rat", "bat", "NO")
]

for st1, st2, ans in tests:
    assert is_anagram(st1, st2) == ans, f"Test {st1}, {st2}, {ans}"
