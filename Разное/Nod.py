import math


def get_nod(num1: int, num2: int) -> int:
    """
    Функция нахождения наибольшего общего делителя двух натуральных чисел (НОД)
    с помощью быстрого алгоритма Евклида

    :param num1: первое натуральное число
    :param num2: второе натуральное число
    :return: НОД
    """

    if num2 > num1:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1


tests = [
    (28, 35),
    (100, 1),
    (2, 10000000),
    (18, 24)
]

for number1, number2 in tests:
    assert get_nod(number1, number2) == math.gcd(number1, number2), f'Test {number1} {number2}'
