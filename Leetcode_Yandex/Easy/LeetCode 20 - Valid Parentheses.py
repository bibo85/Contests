# time complexity - O(n)
# space complexity - O(n)


class Solution:
    def isValid(self, s: str) -> bool:

        # создаем структуру стека
        stack = []

        # создаем пары открывающая:закрывающая скобки

        d_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for elem in s:

            # Если элемент есть в ключах, то это открывающая скобка.
            # Добавляем ее в стек
            if elem in d_map:
                stack.append(elem)

                # если пришла закрывающая скобка, но стек пустой (не открывалась скобка),
                # или последний элемент стека (открывающая скобка) по словарю не бьется с элементом
            elif len(stack) == 0 or d_map[stack.pop()] != elem:
                return False

        return len(stack) == 0
