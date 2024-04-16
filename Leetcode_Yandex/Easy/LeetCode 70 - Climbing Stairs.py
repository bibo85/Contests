# time complexity - O(n)
# space complexity - O(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        # сохраняем промежуточные решения, чтобы избежать лишних вычислений
        memo = {}

        def helper(n, memo):
            if n <= 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
            return memo[n]

        return helper(n, memo)
