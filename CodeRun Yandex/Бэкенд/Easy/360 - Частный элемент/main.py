def main():
    n = int(input())
    nums = list(map(int, input().split()))

    nums_dict = {nums[0]: 1}
    max_freq = nums[0]

    for i in range(1, n):
        cur_num = nums[i]
        nums_dict[cur_num] = 1 + nums_dict.get(cur_num, 0)
        if nums_dict[cur_num] > nums_dict[max_freq]:
            max_freq = cur_num
        elif nums_dict[cur_num] == nums_dict[max_freq]:
            max_freq = cur_num if cur_num > max_freq else max_freq

    print(max_freq)


if __name__ == '__main__':
    main()

tests = [
    # (3, [3, 3, 3], 3),
    # (5, [4, 1, 4, 3, 3], 4),
    # (10, [10, 6, 10, 10, 10, 10, 8, 8, 10, 9], 10),
    # (1, [1], 1),
    # (3, [0, 1, 0], 0),
    # (16, [3, 3, 1, 1, 2, 2, 1, 3, 4, 5, 4, 4, 1, 1, 2, 3], 1),
    # (16, [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2], 2)
]

# for num_cnt, numbers, ans in tests:
#     assert main(num_cnt, numbers) == ans, f'{numbers}'
