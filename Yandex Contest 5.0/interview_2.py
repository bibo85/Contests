# Дана строка s и подстрока p. Необходимо определить, сколько раз в строке встречается анаграмма подстроки

def find_all_anagrams(s: str, p: str) -> int:
    if len(p) > len(s):
        return 0

    maps, mapp = {}, {}
    for i in range(len(p)):
        maps[s[i]] = maps.get(s[i], 0) + 1
        mapp[p[i]] = mapp.get(p[i], 0) + 1

    result = 1 if maps == mapp else 0

    left = 0
    for r in range(len(p), len(s)):
        maps[s[r]] = maps.get(s[r], 0) + 1
        maps[s[left]] -= 1

        if maps[s[left]] == 0:
            maps.pop(s[left])

        left += 1
        if maps == mapp:
            result += 1

    return result
