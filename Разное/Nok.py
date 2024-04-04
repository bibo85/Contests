import math


def get_nok(num1: int, num2: int) -> int:
    """
    Функция нахождения наименьшего общего кратного (НОК) двух положительных чисел
    Формула: НОК = a * b / НОД(a, b)

    :param num1: первое положительное число
    :param num2: второе положительное число
    :return: НОК
    """
    return num1 * num2 // math.gcd(num1, num2)


tests = [
    (5, 10),
    (10, 11),
    (527, 9486)
]

for number1, number2 in tests:
    assert get_nok(number1, number2) == math.lcm(number1, number2), f'Test {number1} {number2}'
