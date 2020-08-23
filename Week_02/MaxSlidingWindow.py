# 59 - I. 滑动窗口的最大值 https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

import collections
from typing import List
class Solution:
    # 双端队列的形式来解决
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        n, res = [], len(nums)
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k,  len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])

        return res

    # 双端队列的形式来解决
    # 思考 [i,j]为一个窗口, i - 1为窗口的前一个元素
    def maxSlidingWindowTwo(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        res = []
        n = len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.pop()
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])
        return res

    # 国际服
    # 思考：问题的难点在于i - k代表什么，k - 1 代表什么
    # i- k 代表 （i - k, i] 是一个窗口  k - 1 是第一个窗口的右边界
    def maxSlidingWindowInternational(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

a = Solution()
print(a.maxSlidingWindowInternational([5,8,3,4,5],2))




