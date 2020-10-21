from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        res = 0
        for i in range(1,n):
            if prices[i] - prices[ i - 1] > 0:
                res += (prices[i] - prices[ i - 1])
        return res
a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))