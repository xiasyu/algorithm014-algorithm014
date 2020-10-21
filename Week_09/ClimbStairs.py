class Solution:
    # 动态规划
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3 , n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


a = Solution()
print(a.climbStairs(4))