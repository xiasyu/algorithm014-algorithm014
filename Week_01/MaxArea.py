class Solution:
    from typing import List
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = height.__len__() - 1
        res = 0
        while i < j:
            area = min(height[i], height[j])*(j-i)
            if area > res:
               res = area
            if height[i] < height[j]:
                i +=1
            else:
                j -= 1
        return res

a = Solution()
print(a.maxArea([1,3,5,2,9]))

              