# A. Эмо бой
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# При регистрации на портале каждый эмо бой обязан придумать себе никнейм. Никнейм должен быть не короче восьми
# символов, содержать в себе хотя бы одну цифру, и хотя бы по одной заглавной и прописной английской букве.
#
# Формат ввода
# Вводится никнейм — последовательность букв и цифр без пробелов. Длина строки не превосходит 100 символов.
#
# Формат вывода
# Выведите «YES», если ник подходит для эмо боя, и «NO» — в противном случае.


def check_nickname(inp_str: str) -> bool:
    if len(inp_str) < 8:
        return False

    is_lower = False
    is_capitalize = False
    is_digit = False

    for s in inp_str:
        if s.islower() and s in alphabet:
            is_lower = True
        elif s.isdigit():
            is_digit = True
        elif s.isupper() and s in alphabet:
            is_capitalize = True

        if all([is_lower, is_capitalize, is_digit]):
            return True
    else:
        return False


alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
nickname = input()
res = check_nickname(nickname)
print("YES") if res else print("NO")


# tests = [
#     ("altushka", False),
#     ("EmObOy2005", True),
#     ("a", False),
#     ("1", False),
#     ("A", False),
#     ("altush1a", False),
#     ("altush1a", False),
#     ("alTush1a", True),
#     ("alfuShaa", False),
#     ("A1r", False),
#     ("A1rae0r", False),
#     ("Arae0rsdfsF", True),
#     ("Бфe0rsdfs", True),
# ]
#
# for i_str, ans in tests:
#     print(f"Выполняется тест {i_str}, {ans}")
#     assert check_nickname(i_str) == ans, f'Test {i_str}, {ans}'

