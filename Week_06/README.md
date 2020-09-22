<a name="index">**Index**</a>
&emsp;<a href="#0">第六周</a>  
&emsp;<a href="#1">动态规划</a>  
&emsp;<a href="#2">模版</a>  
&emsp;&emsp;<a href="#3">递归模版</a>  
<a href="#4">      # process result</a>  
&emsp;&emsp;<a href="#5">分治模版</a>  
&emsp;<a href="#6">递推</a>  
&emsp;<a href="#7">学习方法</a>  
&emsp;<a href="#8">关键点</a>  
&emsp;<a href="#9">动态规划小节</a>  
&emsp;<a href="#10">滚动数组思想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#11">64. 最小路径和</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#12">64. 最小路径和感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#13">62.不同路径</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#14">62.不同路径感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#15">63. 不同路径 II</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#16">63. 不同路径 II感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#17">120.三角形最小路径和</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#18">分治</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#19">动态规划</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#20">53.最大子序列的和</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#21">152.乘积最大子序列</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#22">322. 零钱兑换</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#23">198. 打家劫舍</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#24">198. 打家劫舍感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#25">213. 打家劫舍 II</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#26">213. 打家劫舍 II感想</a>  
[toc]
## <a name="0">第六周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="1">动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="2">模版</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
### <a name="3">递归模版</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
def recursion(level,param1,param2...)
     recursion termimal
    if level > MAX_LEVEL:
        # <a name="4">process result</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        return
     procesa logic in current level
    process(level,data...)
     dill down
    self.recursion(level + 1, p1,...)
    
     restore the current level status if needed
   
```

### <a name="5">分治模版</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1.分治（子问题）
2.状态数组定义
3.DP方程
def divide_conquer(problem, param1, param2...)
     recursion termimal
    if problem is None:
       print_result
       return
     prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem,data)
    
     conquer problems
    subresult1 = self.divide_conquer(subproblems[0],p1...)
    subresult2 = self.divide_conquer(subproblems[1],p1...)
    subresult3 = self.divide_conquer(subproblems[2],p1...)
    ...
    
     process and generate the final result
    result = process_result(subresult1,subresult2,subresult3,...)
       
```
## <a name="6">递推</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

## <a name="7">学习方法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.人肉递归低效，很累
2.找到最近最简方法，将其拆解成可重复解决的问题
3.数学归纳法思维（地址人肉递归的诱惑）
本质：寻找重复性->计算机指令集
## <a name="8">关键点</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
动态规划和递归或者分治没有本质上的区别（关键是看有无最优子结构）
共性：找到重复子问题
差异性：最优子结构，中途可以淘汰次优解
## <a name="9">动态规划小节</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.打破自己的惯性思维，形成及其思维
2.理解复杂逻辑的关键
3.也是职业进阶的要点要领
## <a name="10">滚动数组思想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>



##### <a name="11">64. 最小路径和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
```
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
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for k in range(1,row):
            for l in range(1,col):
                dp[k][l] = min(dp[k - 1][l],dp[k][l - 1]) + grid[k][l]
        return dp[row - 1][col - 1]

a = Solution()
print(a.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))

```

###### <a name="12">64. 最小路径和感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
时间复杂度：o(mn)
1、这道题可以类比最大子序列
2、有点类似于数学归纳法
3、主线路：
   注视：到达 dp[i][j]的方式，只能是 [i - 1][j] 或者 [i][j - 1],所以第一行和第一列，只有一中到达方式，需要特殊考虑
   1) dp[0][0] = grid[0][0]
   2) 当 i > 0 且 j == 0 ，也就是最左边（除[0][0]元素）一行，      行走路径只能是向右移动 所以 dp[i][0] = dp[i - 1][j] + dp[i][0]     
   3) 当 i == 0 且 j > 0 ，也就是最上边（除[0][0]元素）一行，行走路径只能是向右移动 所以 dp[0][j] = dp[0][j - 1] + dp[0][j]
   4) 当 i > 0 且 j > 0, dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) grid[i][j]
       
```
##### <a name="13">62.不同路径</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[62.不同路径](https://leetcode-cn.com/problems/unique-paths/)
```
from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


a = Solution()
print(a.uniquePaths(3,2))
```
###### <a name="14">62.不同路径感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1.最优子结构：opt[n] = best_of(opt(n-1) , opt(n-2), ...)
2.储存中间状态：opt[i]
3.递推公式（美其名曰：状态转移方程或DP方程）
   Fib：opt[i] = opt[n - 1] + opt[n - 2]
   二维路径：opt[i,j] = opt[i + 1,j] + opt[i,j+1]且判断opt[i,j]是否是空地
```

##### <a name="15">63. 不同路径 II</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)
```
class Solution:
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
```
###### <a name="16">63. 不同路径 II感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
此处需要注意：
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
仅当当前不为障碍的时候才能赋值为1，代表可以往下执行。否则直接跳出循环。因为有障碍，下面的都无法到达，所以要跳出循环                
```
##### <a name="17">120.三角形最小路径和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
###### <a name="18">分治</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
python add_lrucache
```
```

###### <a name="19">动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="20">53.最大子序列的和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
暴力法+分治发+DP
```
```
##### <a name="21">152.乘积最大子序列</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
```
##### <a name="22">322. 零钱兑换</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
广度优先遍历
DP
```
```
##### <a name="23">198. 打家劫舍</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        二维数组中 的第二维索引存储的数据为被偷和没有被偷，索引 0:不被偷 索引1:被偷
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i - 1][0],dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[n - 1][0],dp[n - 1][1])
        
        // 第二种方式
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i-2])
        return dp[n - 1]
```
###### <a name="24">198. 打家劫舍感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
动态规划的步骤
1、找到最优子结构
2、储存中间状态
3、递推公式（或者for循环）
第一种方式：
遇到的问题
1、首先要确定 每个房间有两种情况，一种是被偷，一会走是不被偷
2、子问题：第i家房子被偷的情况
    1.在被偷的情况下，a[i][1] = a[i - 1][0] + nums[i], 因为被偷，所  以上家没有被偷才可以
    2.在没有被偷的情况下，a[i][0] = max[a[i - 1][0], a[i - 1][1]],因为没有被偷，所以第i家取得是第i-1家的最大值
    3.最大利益肯定是最后
3.在定义数组的时候一定要注意 x,y关系。也就是二维的关系。因为我们针对的是每一房间被偷盗的情况，所以应该定义为一个 n * 2的数组。python的定义语法胃 [[0] * 2 for _ in range (len(nums))]  n 和 2 的关系一定不能搞反了 

-------------------------------------------  
第二种方式：
dp代表存储状态
第i个房子要么被偷要么没被偷
    1.如果第一个房子被偷，那末dp[i] = dp[i - 1]
    2.如果房子没被偷，那么 dp[i] = num[i] + dp[i - 2]
    3.之所以不考虑 dp[i - 3],dp[i - 4],其实这是子问题，dp[i - 2]肯定大与 dp[i - 3],dp[i - 4]。
    
```

##### <a name="25">213. 打家劫舍 II</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)
```
from typing import List
class Solution:
    def robCycle(self, nums: List[int]) -> int:
        def helper(nums:List[int]):
            pre = 0
            now = 0
            for i in nums:
                now, pre = max(pre + i, now), now
            return now
        return max(helper(nums[:-1]),helper(nums[1:])) if len(nums) != 1 else nums[0]




a = Solution()
print(a.robCycle([1,2,3,1]))
```
###### <a name="26">213. 打家劫舍 II感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
重点：将第一个不被偷和最后一个不被偷拆分开来，拿到最大值
```