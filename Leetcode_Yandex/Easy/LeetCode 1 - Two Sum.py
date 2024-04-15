# time complexity - O(n)
# space complexity - O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # числа, которые мы видели и их индексы: {число:индекс}
        seen = {}

        for i, val in enumerate(nums):
            # вычисляем, сколько нам не хватает, чтобы получить target
            remaining = target - val

            # если нужный остаток есть в уже просмотренных, то нашли ответ
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[val] = i
