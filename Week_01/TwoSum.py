class Solution:
    def __init__(self):
        pass

    from typing import List
    # 第一种方式 o(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        different = []
        for i in range(0, len(nums)):
            value = target - nums[i]
            different.append(value)
        for i in range(0, len(nums)):
            for j in range(0, len(different)):
                if (nums[i] == different[j]) & (i != j):
                    return [i,j]
        return [0,0]     

     
     # 第二种方式 遍历法
    def twoSumTwo(self, nums: List[int], target: int) -> List[int]:          
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0,0]
    
    # 第三种方式 hash方式实现
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        tempdict = {}
        for i in range(0, len(nums)):
            tempdict[nums[i]] = i
        for i in range(0, len(nums)):
            value = target - nums[i]
            if (value in tempdict) & (i != tempdict[value]):
                return [i, tempdict[value]]
        return [0,0]  

    # 第四种方式 哈希方式 不是很好理解 （这个方式的理解，可以理解为 原始序列和差的map是逆序的，相当，一定存在一前一后的问题。一个的出现必定在另一个的后面）
    def twoSumHashTwo(self, nums: List[int], target: int) -> List[int]:
        tempHash = {}
        for i in range(0, len(nums)):
            value = target - nums[i]
            print(value,tempHash)
            if value in tempHash:
                return [tempHash[value],i]
            tempHash[nums[i]] = i   
             

a = Solution()
print(a.twoSumHash([3,4,11,5],8))