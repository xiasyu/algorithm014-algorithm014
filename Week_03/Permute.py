from typing import List
import collections
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n == 0:
            return res
        path = []
        used = [0] * n
        self.dfs(nums, n, 0, path, used, res)
        return res

    def dfs(self, nums: List[int], n: int, depth:int, path:List[int], used: List[bool], res: List[List[int]]):
        if depth == n:
            res.append(path.copy())
            return ;
        for i in range(n):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.dfs(nums, n, depth + 1, path, used, res)
            path.pop()
            used[i] = False

a = Solution()
print(a.permute([1,2]))