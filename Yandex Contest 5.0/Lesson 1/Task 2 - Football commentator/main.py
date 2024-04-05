# Футбольный комментатор
#
# Ограничение времени	2 секунды
# Ограничение памяти	64Mb
#
# Раунд плей-офф между двумя командами состоит из двух матчей. Каждая команда проводит по одному матчу «дома» и
# «в гостях». Выигрывает команда, забившая большее число мячей. Если же число забитых мячей совпадает,
# выигрывает команда, забившая больше мячей «в гостях». Если и это число мячей совпадает, матч переходит в
# дополнительный тайм или серию пенальти.
#
# Вам дан счёт первого матча, а также счёт текущей игры (которая ещё не завершилась). Помогите комментатору сообщить,
# сколько голов необходимо забить первой команде, чтобы победить, не переводя игру в дополнительное время.
#
# Формат ввода
# В первой строке записан счёт первого мачта в формате G1:G2, где G1 — число мячей, забитых первой командой,
# а G2 — число мячей, забитых второй командой.
# Во второй строке записан счёт второго (текущего) матча в аналогичном формате. Все числа в записи счёта не превышают 5.
# В третьей строке записано число 1, если первую игру первая команда провела «дома», или 2, если «в гостях».
#
# Формат вывода
# Выведите единственное целое число — необходимое количество мячей.
#
# Пример 1
# Ввод
# 0:0
# 0:0
# 1
# Вывод
# 1
#
# Пример 2
# Ввод
# 0:2
# 0:3
# 1
# Вывод
# 5
#
# Пример 3
# Ввод
# 0:2
# 0:3
# 2
# Вывод
# 6

with open('input.txt', 'r', encoding='utf-8') as file:
    games = [list(map(int, line.rstrip().split(':'))) for line in file]
    first_team_score = []
    second_team_score = []

    if games[2][0] == 1:
        for i in range(2):
            first_team_score.append(games[i][0])
            second_team_score.append(games[1 - i][1])
    else:
        for i in range(2):
            first_team_score.append(games[1 - i][0])
            second_team_score.append(games[i][1])

    if sum(first_team_score) == sum(second_team_score):
        if first_team_score[1] == second_team_score[1]:
            print(1)
        else:
            if first_team_score[1] > second_team_score[1]:
                print(0)
            else:
                print(1)
    elif sum(second_team_score) - sum(first_team_score) < 0:
        print(0)
    else:
        diff = abs(sum(first_team_score) - sum(second_team_score))
        if games[2][0] == 1:
            if diff + first_team_score[1] > second_team_score[1]:
                print(diff)
            else:
                print(diff + 1)
        else:
            if first_team_score[1] > second_team_score[1]:
                print(diff)
            else:
                print(diff + 1)
