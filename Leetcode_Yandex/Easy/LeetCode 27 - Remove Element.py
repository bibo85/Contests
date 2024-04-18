# time complexity - O(n)
# space complexity - O(1)

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i, j = 0, 0

        while j < len(nums):

            if nums[i] == val and nums[j] == val:
                j += 1
                continue
            elif nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

        return i
