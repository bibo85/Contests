# Ограничение времени 1 секунда
# Ограничение памяти 64Mb
#
# Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка
# больше предыдущего).
#
# Выведите YES, если массив монотонно возрастает и NO в противном случае.

def check_lst(lst: list) -> bool:
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    else:
        return True


inp_lst: list[int] = list(map(int, input().split()))
res = check_lst(inp_lst)

print("YES") if res else print("NO")
