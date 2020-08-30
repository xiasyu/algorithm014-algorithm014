from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n < k or k <= 0:
            return res
        res = self.combine(n -1, k - 1)
        if len(res) == 0:
            res.append([])
        for list in res:
            list.append(n)
        res = res + self.combine(n - 1, k)
        return res

a = Solution()
print(a.combine(4,2))