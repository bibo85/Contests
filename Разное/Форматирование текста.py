# Ограничение времени	1 секунда
# Ограничение памяти	256.0 Мб

# Если вы используете язык C++, то для считывания входных данных в этой задаче вам может понадобиться функция
# std::getline.
#
# Дан текст из строчных английских букв, пробелов и запятых. Пусть len равно максимальной длине слова в тексте,
# умноженной на 3. Вам необходимо отформатировать текст следующим образом:#
#  - в каждой строке должно быть не более len символов
#  - запятая «приклеивается» к слову перед ней, то есть должна находиться на одной строке с ним
#  - перед запятой пробел не ставится
#  - после запятой пробел ставится, если она не является последним символом строки
#  - если слово не входит на строку i, строка i заканчивается, а слово будет записано на строке (i+1)
#  - последним символом в любой строке должна быть буква или запятая
#
# Формат ввода
# В единственной строке ввода находится строка w (1 ≤ ∣w∣ ≤ 10**5) из строчных английских букв, запятых и пробелов.
#
# Гарантируется, что:
#  - в тексте между любыми двумя запятыми есть непустое слово
#  - текст начинается с буквы
#  - в тексте нет двух пробелов подряд
#
# Формат вывода
# Выведите текст, отформатированный в соответствии с условием задачи.
#
# Пример 1
# Ввод
# once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched
#
# Вывод
# once upon a time, in a land
# far far away lived a
# princess, whose beauty was
# yet unmatched
#
# Пример 2
# Ввод
# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex
#
# Вывод
# a, b, c, d, e, f,
# g, h, i, j, k, l,
# m, n, o, p, yandex


def main():
    text = input()
    if len(text) == 1:
        return text

    text_formated = []
    word = ""
    word_max_length = 0
    for elem in text:
        if elem == " " and word:
            text_formated.append(word)
            word_max_length = max(word_max_length, len(word))
            word = ""
        elif elem == " " and not word:
            continue
        elif elem == ",":
            if word:
                word_max_length = max(word_max_length, len(word))
                word = word + ","
                text_formated.append(word)
                word = ""
            else:
                last_word = text_formated.pop()
                new_word = last_word + ","
                text_formated.append(new_word)
        else:
            word += elem
    word_max_length = max(word_max_length, len(word))
    text_formated.append(word)

    line_max_length = word_max_length * 3
    res = []
    line = ""
    for elem in text_formated:
        if len(elem) + len(line) > line_max_length:
            res.append(line.strip())
            line = elem + " "
        else:
            line += elem + " "
    res.append(line.strip())

    return "\n".join(res)


if __name__ == '__main__':
    ans = main()
    print(ans)
