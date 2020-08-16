# [15.三数之和](https://leetcode-cn.com/problems/3sum/)
class Solution:
    def __init__(self):
        pass

    from typing import List
    #第一种做法：暴力
    def threeSums(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [i, j, k]


    # 第二种做法：双指针法
    def threeSumSort(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for first in range(0, len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            third = len(nums) - 1
            target = -nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -=  1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans            




a = Solution()
print(a.threeSums([1,2,3,-4]))
print(a.threeSumSort([1,2,3,-4]))