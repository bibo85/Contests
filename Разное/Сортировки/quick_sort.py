# быстрая сортировка

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot, less, greater = supp_func(arr)

    return quicksort(less) + pivot + quicksort(greater)


def supp_func(arr):
    pivot = [num for num in arr if num == arr[-1]]
    less = [num for num in arr if num < arr[-1]]
    greater = [num for num in arr if num > arr[-1]]
    return pivot, less, greater


numbers = [5, 8, 9, 4, 2, 9, 1, 8]
print(quicksort(numbers))
