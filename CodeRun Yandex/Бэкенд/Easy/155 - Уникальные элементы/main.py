def main():
    num_cnt = int(input())
    nums = list(map(int, input().split()))

    hmap = {}
    for num in nums:
        hmap[num] = hmap.get(num, 0) + 1

    count = 0
    for key in hmap:
        if hmap[key] > 1:
            count += hmap[key]
    print(num_cnt - count)


if __name__ == '__main__':
    main()
