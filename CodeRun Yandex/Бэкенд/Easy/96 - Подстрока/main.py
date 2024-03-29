def main():
    cnt, max_k = map(int, input().split())
    string = input()

    map_s = {}

    max_length = 0
    idx = 0
    l = 0
    for r in range(cnt):
        map_s[string[r]] = map_s.get(string[r], 0) + 1
        if map_s[string[r]] > max_k:
            while map_s[string[r]] != map_s[string[l]]:
                map_s[string[l]] -= 1
                l += 1
            map_s[string[l]] -= 1
            l += 1
        length = r - l + 1
        if length > max_length:
            max_length = length
            idx = l

    print(max_length, idx + 1)


if __name__ == '__main__':
    main()
