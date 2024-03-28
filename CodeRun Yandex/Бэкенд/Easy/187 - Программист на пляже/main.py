def main():
    cnt = int(input())

    for _ in range(cnt):
        nums_cnt = int(input())
        nums = sorted(list(map(int, input().split())))

        result = nums[0] ^ nums[1]
        for i in range(1, nums_cnt):
            result = min(result, nums[i - 1] ^ nums[i])
        print(result)


if __name__ == '__main__':
    main()
