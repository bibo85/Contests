# time complexity - O(n)
# space complexity - O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            # считаем текущий профит и обновляем максимум
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            # проверяем, есть ли справа лучший вариант
            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit
