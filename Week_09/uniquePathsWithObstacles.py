from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 思路跟没有障碍的机器人走到重点类似，区别就在于，当有障碍的时候不需要进行计算
        # 在定义dp的时候我们需要将障碍也初始化进去
        row = len(obstacleGrid)
        if row == 0:
            return 0
        col = len(obstacleGrid[0])
        dp = [[0] * col for _ in range(row)]

        # 初始化第一行
        for i in range(row):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else: # 有障碍则无需在初始化，因为第一行只能横向，有障碍横向通不过
                break

        for j in range(col):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for k in range(1, row):
            for l in range(1, col):
                if obstacleGrid[k][l] == 0:
                    dp[k][l] = dp[k - 1][l] + dp[k][l - 1]

        return dp[row - 1][col - 1]

a = Solution()
print(a.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
