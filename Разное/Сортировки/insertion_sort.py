# Сортировка вставками
#
# Сортировка вставками (insertion sort) — это простой алгоритм сортировки, который постепенно строит отсортированную
# последовательность, один элемент за другим, вставляя каждый новый элемент в правильное место.
#
# Преимущества сортировки вставками:
# - Простота реализации. Сортировка вставками — один из наиболее простых алгоритмов сортировки для понимания и
#   реализации. Она требует только базовых операций сравнения и перестановки элементов.
# - Эффективность для малых размеров. Для небольших списков или уже частично упорядоченных данных сортировка вставками
#   может быть эффективнее, чем другие алгоритмы сортировки, такие как сортировка слиянием или быстрая сортировка.
#   Она имеет низкую структурную сложность и минимальные накладные расходы при обработке небольшого количества
#   элементов.
# - Адаптивность. Сортировка вставками адаптивна, что означает, что её производительность может улучшаться для частично
#   упорядоченных данных. Она может быстро обрабатывать уже отсортированные или почти отсортированные списки.
#
# Недостатки алгоритма сортировки вставками:
# - Квадратичная сложность алгоритма. Время выполнения растёт пропорционально квадрату количества элементов, что может
#   привести к плохой производительности при больших наборах данных.
# - Зависимость от исходного порядка. Алгоритм неэффективен при обратно отсортированных данных или данных, где элементы
#   уже находятся на своих местах.
# - Неустойчивость. Может изменять относительный порядок элементов с одинаковыми значениями, если это важно для
#   конкретной задачи.

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        # берем текущий элемент, который нужно вставить в отсортированную часть списка
        key = lst[i]
        j = i - 1

        # перемещаем элементы, которые больше key, на одну позицию вперед
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        # вставляем key в правильное место
        lst[j + 1] = key


if __name__ == '__main__':
    numbers = [5, 3, 8, 2, 1]
    insertion_sort(numbers)
    print(numbers)
