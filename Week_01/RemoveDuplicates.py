class Solution:
    from typing import List
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        count = 0
        for i in range(1, len(nums)):
            # 不等的时候将i的值存储到 ++j上
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            else:
                 count += 1   
        print(nums)        
        return len(nums) - count
a = Solution()
print(a.removeDuplicates([1,1,2,3,4,4,5]))