from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        maxRes = 0
        for i in range(len(dp)):
            if dp[i] > maxRes:
                maxRes = dp[i]
        return maxRes

    # # 这个方法没有看明白
    # def lengthOfLIS(self, nums):
    #     tails = [0] * len(nums)
    #     size = 0
    #     for x in nums:
    #         i, j = 0, size
    #         while i != j:
    #             m = (i + j) // 2
    #             if tails[m] < x:
    #                 i = m + 1
    #             else:
    #                 j = m
    #         tails[i] = x
    #         size = max(i + 1, size)
    #     return size
a = Solution()
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))
