from typing import List
class Solution:
    # 第一种方法
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for a in range(1,m):
            for k in range(1,n):
                if obstacleGrid[a][k] == 0:
                    dp[a][k] = dp[a - 1][k] + dp[a][k - 1]
        return dp[m - 1][n - 1]


a = Solution()
print(a.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))