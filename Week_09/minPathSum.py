from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1,row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1,col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for k in range(1,row):
            for l in range(1,col):
                dp[k][l] = min(dp[k - 1][l], dp[k][l - 1]) + grid[k][l]
        return dp[row - 1][col - 1]

a = Solution()
print(a.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))