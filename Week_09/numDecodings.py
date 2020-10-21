from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1,n):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                if i - 2 >= 0:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1
        return dp[n - 1]

a = Solution()
print(a.numDecodings('212'))
