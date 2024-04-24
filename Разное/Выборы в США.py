# Выборы в США
#
# Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. Сначала
# проводятся выборы в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные
# выборы: на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата. На практике,
# все выборщики от штата голосуют в соответствии с результами голосования внутри штата, то есть на заключительной стадии
# выборов в голосовании участвуют штаты, имеющие различное число голосов. Вам известно за кого проголосовал каждый штат
# и сколько голосов было отдано данным штатом. Подведите итоги выборов: для каждого из участника голосования определите
# число отданных за него голосов.
#
# Формат ввода
# Каждая строка входного файла содержит фамилию кандидата, за которого отдают голоса выборщики этого штата, затем через
# пробел идет количество выборщиков, отдавших голоса за этого кандидата.
#
# Формат вывода
# Выведите фамилии всех кандидатов в лексикографическом порядке, затем, через пробел, количество отданных за них
# голосов.

with open("input.txt", "r", encoding="utf-8") as file:
    candidats = {}

    for line in file.readlines():
        name, votes = line.split()
        candidats[name] = candidats.get(name, 0) + int(votes)

    candidats_lst = sorted([(n, v) for n, v in candidats.items()])

    for candidat in candidats_lst:
        print(f"{candidat[0]} {candidat[1]}")
