# time complexity - O(n)
# space complexity - O(1)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # отслеживает левую границу неповторяющихся значений
        i = 0

        for j in nums[1:]:

            # если встретили новый элемент, то сдвигаем указатель и заносим туда это значение
            if nums[i] != j:
                i += 1
                nums[i] = j

        # возвращаем длину, поэтому увеличиваем на 1
        return i + 1
