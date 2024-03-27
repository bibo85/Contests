# Замена слов
#
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте. Для этого был
# составлен словарь слов, до которых можно сокращать более длинные слова. Слово из текста можно сократить, если в
# словаре найдется слово, являющееся началом слова из текста. Например, если в списке есть слово "лом", то слова из
# текста "ломбард", "ломоносов" и другие слова, начинающиеся на "лом", можно сократить до "лом".
#
# Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого
# короткого слова.
#
# Формат ввода
# В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв. Гарантируется,
# что словарь не пуст и количество слов в словаре не превышет 1000, а длина слов — 100 символов.
#
# Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв).
# Количество слов в тексте не превосходит 105, а суммарное количество букв в них — 106.
#
# Формат вывода
# Выведите текст, в котором осуществлены замены.
#
# Пример 1
# Ввод
# a b
# abdafb basrt casds dsasa a
#
# Вывод
# a b casds dsasa a
#
# Пример 2
# Ввод
# aa bc aaa
# a aa aaa bcd abcd
#
# Вывод
# a aa aa bc abcd


def main(wd, words_lst):
    hash_set = set()
    max_length = 0
    for i_word in wd:
        length_pref = len(i_word)
        hash_set.add(i_word)
        if length_pref > max_length:
            max_length = length_pref

    res = []
    for word in words_lst:
        for i in range(1, max_length + 1):
            if word[:i] in hash_set:
                res.append(word[:i])
                break
        else:
            res.append(word)

    return " ".join(res)


with open('input.txt', 'r', encoding='utf-8') as file:
    words_dict = list(file.readline().split())
    words = list(file.readline().split())
ans = main(words_dict, words)
print(ans)

# tests = [
#     (["a", "b"], ["abdafb", "basrt", "casds", "dsasa", "a"], ["a", "b", "casds", "dsasa", "a"]),
#     (["aa", "bc", "aaa"], ["a", "aa", "aaa", "bcd", "abcd"], ["a", "aa", "aa", "bc", "abcd"]),
#     (["лом"], ["ломбард", "ломоносов"], ["лом", "лом"]),
# ]
# # #
# for words_dict, words, ans in tests:
#     assert main(words_dict, words) == ans, f'Test {words_dict}, {words}, {ans}'
