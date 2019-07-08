class Solution:
    def climbStairs(self, n, memo = {}):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2

        elif n in memo:
            return memo[n]

        else:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
            return memo[n]

sol  = Solution()
print(sol.climbStairs(3))