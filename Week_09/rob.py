from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1、突破点是dp[i][0] = max(dp[i - 1][0],dp[i - 1][1])
        # 2、dp[i][1] = dp[i - 1][0] + num[i]

        n = len(nums)
        if n == 0:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[n - 1][0],dp[n - 1][1])

a = Solution()
print(a.rob([2,7,9,3,1]))