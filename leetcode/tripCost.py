class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        start0 = cost[0]
        start1 = cost[1]
        for c in range(2, len(cost)):
            start0, start1 = start1, min(start0, start1) + cost[c]

        return min(start0, start1)


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sol = Solution()
print(sol.minCostClimbingStairs(cost))