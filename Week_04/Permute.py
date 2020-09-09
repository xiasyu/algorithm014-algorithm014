from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 0:
            return []
        used = [False] * n
        res = []
        path = []
        self.dfs(nums, n,0,used,res,path)
        return res

    def dfs(self, nums:List[int], n:int, depth:int, used:List[bool],res:List[List[int]],path:List[int]):
        if n == depth:
            res.append(path.copy())
            return res
        for i in range(n):
            if used[i] == False:
                path.append(nums[i])
                used[i] = True
                self.dfs(nums,n,depth + 1,used,res,path)
                used[i] = False
                path.pop()
a = Solution()
print(a.permute([1,2,3]))