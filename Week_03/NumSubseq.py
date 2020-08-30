from typing import List
import bisect
class Solution:
    #
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10 ** 9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P


        nums.sort()
        ans = 0
        for i,num in enumerate(nums):
            if 2 * nums[i] > target:
                break
            max = target - nums[i]
            pos = bisect.bisect_right(nums,max) - 1
            contribute = f[pos - i] if pos >= i else 0
            ans += contribute
        return  ans % P

    # 双指针
    def numSubseqDoublePointer(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10**9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P

        ans = 0
        nums.sort()
        i = 0
        j = n - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                ans = (ans + f[j - i]) % P
                i += 1

        return ans



a = Solution()
print(a.numSubseqDoublePointer([5,2,4,1,7,6,8],16))