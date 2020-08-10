
class Solution:

    # 方法一  递归
    def climbStairs(n: int) -> int:
       dp = {}
       dp[1] = 1
       dp[2] = 2
       for i in range(3, n + 1):
           dp[i] = dp[i - 1] + dp[i - 2]
       return dp[n]

        # 方法二 动态规划
    def ClimbStairsDyanmic(n:int) -> int: 

        p = 0
        q = 0
        r = 1
        for i in range(1,n + 1):
            p = q
            q = r
            r = p + q
        return r

    num = ClimbStairsDyanmic(3) 
    print( " \lClimbStairsDyanmic楼梯 =", num)

class Solution:

    def __init__(self):
        pass

    # 方法三 递归缓存
    def climbStairs(self, n: int) -> int:
        return self.ClimbStarirsCatch(n, [0] * (n + 1))

    def ClimbStarirsCatch(self, n: int, arr) -> int:
        if n == 1:
            arr[1] = 1
            return 1
        if n == 2:
            arr[2] = 2
            return 2
        if arr[n] != 0:
            return arr[n]
        else:
            arr[n] = self.ClimbStarirsCatch(
                n - 1, arr) + self.ClimbStarirsCatch(n - 2, arr)
        return arr[n]

a = Solution()
print( " \l楼梯 =", a.climbStairs(3))

