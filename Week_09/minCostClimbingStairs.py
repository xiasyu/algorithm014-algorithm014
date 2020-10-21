from typing import List
class Solution:
    # 这个方法没咋理解

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # f[i] = cos[i] + min(f[i + 1], f[i + 2])
    #     f1 , f2 = 0, 0
    #     for x in reversed(cost):
    #         f1, f2 = x + min(f1, f2), f1
    #     return min(f1,f2)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
        return min(dp[-1] , dp[-2])

a = Solution()
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

