from typing import List
class Solution:
    def robCycle(self, nums: List[int]) -> int:
        def helper(nums:List[int]):
            pre = 0
            now = 0
            for i in nums:
                now, pre = max(pre + i, now), now
            return now
        return max(helper(nums[:-1]),helper(nums[1:])) if len(nums) != 1 else nums[0]




a = Solution()
print(a.robCycle([1,2,3,1]))