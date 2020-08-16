# [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
class Solution:
    from typing import List
    # 第一种解法
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            # 不等的时候将i的值存储到 ++j上
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i] 
        return j + 1

a = Solution()
print(a.removeDuplicates([1,1,2,3,4,4,5]))