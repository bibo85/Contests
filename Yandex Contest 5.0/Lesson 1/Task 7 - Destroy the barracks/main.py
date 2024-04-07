# Разрушить казарму
#
# Ограничение времени	1 секунда
# Ограничение памяти	256Mb
#
# Вы играете в интересную стратегию. У вашего соперника остались всего одна казарма — здание, в котором постоянно
# появляются новые солдаты. Перед атакой у вас есть x солдат. За один раунд каждый солдат может убить одного из
# солдат противника или нанести 1 очко урона казарме (вычесть единицу здоровья у казармы). Изначально у вашего
# оппонента нет солдат. Тем не менее, его казарма имеет y единиц здоровья и производит p солдат за раунд.
#
# Ход одного раунда:
#   1. Каждый солдат из вашей армии либо убивает одного из солдат вашего противника, либо наносит 1 очко урона казарме.
#      Каждый солдат может выбрать своё действие. Когда казарма теряет все свои единицы здоровья, она разрушается.
#   2. Ваш противник атакует. Он убьет k ваших солдат, где k — количество оставшихся у противника солдат.
#   3. Если казармы еще не разрушены, ваш противник производит p новых солдат.
#
# Ваша задача — разрушить казарму и убить всех солдат противника. Если это возможно, посчитайте минимальное количество
# раундов, которое вам нужно для этого. В противном случае выведите -1.
#
# Формат ввода
# На вход подаётся три целых числа x, y, p (1 ≤ x, y, p ≤ 5000) — количество ваших солдат на старте игры, количество
# очков здоровья казармы и количество производимых за раунд казармой солдат, соответственно. Каждое число расположено
# в новой строке.
#
# Формат вывода
# Если возможно убить всех вражеских солдат и разрушить казарму, выведите минимальное количество раундов, необходимых
# для этого. В противном случае выведите -1.
#
# Пример 1
# Ввод
# 10
# 11
# 15
#
# Вывод
# 4
#
# Пример 2
# Ввод
# 1
# 2
# 1
#
# Вывод
# -1
#
# Пример 3
# Ввод
# 1
# 1
# 1
#
# Вывод
# 1
#
# Пример 4
# Ввод
# 25
# 200
# 10
#
# Вывод
# 13
#
# Примечания
# В первом примере в первом раунде сначала все ваши солдаты атакуют казарму, после этого не происходит ничего, потому
# что у врага нет солдат, затем у врага появляется 15 солдат. Во втором раунде один ваш солдат добивает казарму,
# остальные 9 солдат убивают 9 солдат врага. Оставшиеся 6 солдат врага убивают 6 ваших солдат, но армия врага не
# пополняется, поскольку казарма разрушена. В третьем раунде сначала вы убиваете четверых солдат врага, затем враг
# двоих ваших солдат. В последнем, четвертом, раунде вы добиваете двух оставшихся солдат врага.

def is_win(damage_soldiers, damage_enemy):
    cnt = 0
    while damage_soldiers > 0 and damage_enemy > 0:
        cnt += 1
        damage_enemy -= damage_soldiers
        damage_soldiers -= damage_enemy
    return damage_soldiers > 0, cnt


with open('input.txt', 'r', encoding='utf-8') as file:
    soldiers, barracks_health, enemy_soldiers_multiplier = map(int, file.readlines())
    enemy_soldiers = 0

    i = 0
    if enemy_soldiers == 0:
        i += 1
        barracks_health -= soldiers
        if barracks_health > 0:
            enemy_soldiers += enemy_soldiers_multiplier

    while enemy_soldiers > 0 or barracks_health > 0:
        i += 1

        if barracks_health <= 0:
            enemy_soldiers -= soldiers
            soldiers -= enemy_soldiers if enemy_soldiers > 0 else 0
        else:
            if enemy_soldiers + barracks_health <= soldiers:
                enemy_soldiers = 0
                barracks_health = 0
            else:
                after_attack = soldiers - barracks_health
                attack_enemy = enemy_soldiers - after_attack
                res = 0
                counter = 0
                if after_attack > 0:
                    res, counter = is_win(soldiers - attack_enemy, attack_enemy)

                if res:
                    enemy_soldiers = enemy_soldiers_multiplier
                    barracks_health -= soldiers - enemy_soldiers
                    after_attack = soldiers - barracks_health
                    attack_enemy = min(enemy_soldiers - after_attack, soldiers)
                    res2, counter2 = is_win(soldiers - attack_enemy, enemy_soldiers - after_attack)
                    if res2 and counter2 < counter:
                        i += counter2 + 1
                    else:
                        i += counter
                    break
                else:
                    attack_enemy = min(enemy_soldiers, soldiers)
                    enemy_soldiers -= attack_enemy
                    barracks_health -= soldiers - attack_enemy
                    soldiers -= enemy_soldiers

        if barracks_health > 0:
            enemy_soldiers += enemy_soldiers_multiplier

        if soldiers <= 0 or (soldiers == enemy_soldiers_multiplier and barracks_health > 0):
            i = -1
            break

    print(i)
