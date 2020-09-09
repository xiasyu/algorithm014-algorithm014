from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pre = 0
        dict = {pre:1}
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            target = pre - k
            if target in dict.keys():
                count += dict[target]

            if pre in dict.keys():
                dict[pre] = dict[pre] + 1
            else:
                dict[pre] = 1
        return count
a = Solution()
print(a.subarraySum([1,1,1],2))
