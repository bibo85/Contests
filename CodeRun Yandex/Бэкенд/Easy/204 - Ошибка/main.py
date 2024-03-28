def main():
    count = int(input())

    total_sum = 0
    nums = []
    for i in range(count):
        num1, num2 = map(int, input().split())
        res = num1 * num2
        nums.append(res)
        total_sum += res

    for i in range(count):
        print(round(nums[i] / total_sum, 9))


if __name__ == '__main__':
    main()
