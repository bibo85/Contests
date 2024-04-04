def fibonacci(n: int) -> int:
    """
    Функция вычисление n-го числа ряда Фибоначчи
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


tests = [
    (5, 5),
    (2, 1),
    (0, 0),
    (1, 1)
]

for number, ans in tests:
    assert fibonacci(number) == ans, f'Test {number}: {ans}'
