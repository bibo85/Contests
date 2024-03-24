# Известный художник
#
# Ограничение по времени: 1 секунда
# Ограничение по памяти на тест: 256 мб


def find_max_cortrast(nums_cnt, nums_lst):
    idx_min = 0
    idx_max = 0

    for i in range(n):
        if nums[i] < nums[idx_min]:
            idx_min = i
        if nums[i] >= nums[idx_max]:
            idx_max = i
    return [idx_max + 1, idx_min + 1]


with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    nums = list(map(int, file.readline().split()))
    ans = find_max_cortrast(n, nums)
    print(*ans)

# Test
# tests = [
#     (6, [1, 2, 1, 3, 1, 3], [6, 1]),
#     (4, [2, 1, 0, -1], [1, 4])
# ]
#
# for n, nums, ans in tests:
#     assert find_max_cortrast(n, nums) == ans
