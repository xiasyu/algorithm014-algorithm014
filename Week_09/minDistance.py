from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for k in range(1,m + 1):
            for l in range(1,n + 1):
                if word1[k - 1] == word2[l - 1]:
                    dp[k][l] = dp[k - 1][l - 1]
                else:
                    dp[k][l] = min(dp[k - 1][l], dp[k][l - 1],dp[k - 1][l - 1]) + 1
        return dp[m][n]
a = Solution()
print(a.minDistance("intention","execution"))

