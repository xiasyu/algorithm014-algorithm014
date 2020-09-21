from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 0:
        #     return 0
        # dp = [[0]*2 for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = nums[0]
        # for i in range(1,len(nums)):
        #     dp[i][0] = max(dp[i - 1][0],dp[i - 1][1])
        #     dp[i][1] = dp[i - 1][0] + nums[i]
        #
        # return max(dp[n - 1][0],dp[n - 1][1])

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i-2])
        return dp[n - 1]







a = Solution()
print(a.rob([1,2,3,1]))