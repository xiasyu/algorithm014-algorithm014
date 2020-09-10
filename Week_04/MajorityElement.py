from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        halfN = n // 2
        print(halfN)
        dict = {}
        for i in range(n):
            currentNum = nums[i]
            value = 1
            if currentNum in dict:
                value = dict[currentNum]
                value += 1
            if value > halfN:
                return currentNum
            dict[currentNum] = value
            sorted()
        return -1


a = Solution()
print(a.majorityElement( [1]))