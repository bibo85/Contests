# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
#
# Вася решил заняться торговлей рыбой. С помощью методов машинного обучения он предсказал цены на рыбу на N дней вперёд.
# Он решил, что в один день он купит рыбу, а в один из следующих дней — продаст (то есть совершит или ровно одну покупку
# и продажу или вообще не совершит покупок и продаж, если это не принесёт ему прибыли).
# К сожалению, рыба — товар скоропортящийся и разница между номером дня продажи и номером дня
# покупки не должна превышать K.
# Определите, какую максимальную прибыль получит Вася.
#
# Формат ввода
# В первой строке входных данных задаются числа N и K (1 ≤ N ≤ 10000, 1 ≤ K ≤ 100).
#
# Во второй строке задаются цены на рыбу в каждый из N дней. Цена — целое число,
# которое может находиться в пределах от 1 до 109.

# Формат вывода
# Выведите одно число — максимальную прибыль, которую получит Вася.

# Пример 1
# Ввод
# 5 2
# 1 2 3 4 5

# Вывод
# 2

# Пример 2
# Ввод
# 5 2
# 5 4 3 2 1

# Вывод
# 0


with open('input.txt', 'r', encoding='utf-8') as file:
    days, k_days = map(int, file.readline().split())
    prices = list(map(int, file.readline().split()))

    ans = 0

    # Идем по каждому дню и проверяем выполнение условия, но не более k_days дней вперед
    for i in range(days - 1):
        for j in range(i + 1, min(i + k_days + 1, days)):
            if prices[i] < prices[j]:
                ans = max(ans, prices[j] - prices[i])

    print(ans)
