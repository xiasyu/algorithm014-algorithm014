from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in  range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                four = len(nums) - 1
                for three in range(second + 1, len(nums)):
                    if three > second + 1 and nums[three] == nums[three - 1]:
                        continue
                    while three < four and nums[second] + nums[three] + nums[four] + nums[first] > target:
                        four -= 1
                    if three == four:
                        break
                    if nums[second] + nums[three] + nums[four] + nums[first] == target:
                        res.append([nums[first],nums[second],nums[three],nums[four]])
        return res

a = Solution()
print(a.fourSum([1,0,-1,0,-2,2],0))