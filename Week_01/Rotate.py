# [189.旋转数组 (第三种方式没有看懂)](https://leetcode-cn.com/problems/rotate-array/)
class Solution:
    from typing import List
    # 这个方法耗时
    def rotate(self, nums: List[int], k: int) -> List[int]:
        k = k % len(nums)
        if k >= len(nums):
            return nums
        for i in range(0,k):
            nums.insert(0,nums[len(nums) - 1 - i])   

        for i in range(0, k):
            nums.pop()  
        return nums      
        

    def rotateTwo(self, nums: List[int], k: int) -> List[int]:
        temp = 0 
        previpus = 0
        k = k % len(nums)
        if k >= len(nums):
            k = k - len(nums)
        for i in range(0,k):
            previpus = nums[-1]
            for j in range(0, len(nums)):
                temp = nums[j]
                nums[j] = previpus
                previpus = temp
        return nums

    # 第三种解法： 使用环状替换
    # 思路：因为
    def rotateThree(self, nums: List[int], k: int) -> List[int]:
        k = k % len(nums)
        count = 0
        for start in range(0, len(nums)):
            if count >= len(nums):
                return nums
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break
        return nums


a = Solution()
# print(a.rotate([1,2,3,4,5],4))
# print(a.rotateTwo([1,2,3,4,5],2),'\n')
print(a.rotateThree([1,2,3,4,5,6],2))

 
       