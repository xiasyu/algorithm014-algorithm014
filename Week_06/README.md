<a name="index">**Index**</a>
&emsp;<a href="#0">第六周</a>  
&emsp;<a href="#1">动态规划</a>  
&emsp;<a href="#2">模版</a>  
&emsp;&emsp;<a href="#3">递归模版</a>  
<a href="#4">      # process result</a>  
&emsp;&emsp;<a href="#5">分治模版</a>  
&emsp;<a href="#6">递推</a>  
&emsp;<a href="#7">学习方法</a>  
&emsp;<a href="#8">动态规划小节</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#9">64. 最小路径和</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#10">64. 最小路径和感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#11">62.不同路径</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#12">62.不同路径感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#13">120.三角形最小路径和</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#14">分治</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#15">动态规划</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#16">53.最大子序列的和</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#17">152.乘积最大子序列</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#18">322. 零钱兑换</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#19">198. 打家劫舍</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#20">198. 打家劫舍感想</a>  

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
##关键点
动态规划和递归或者分治没有本质上的区别（关键是看有无最优子结构）
共性：找到重复子问题
差异性：最优子结构，中途可以淘汰次优解
## <a name="8">动态规划小节</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.打破自己的惯性思维，形成及其思维
2.理解复杂逻辑的关键
3.也是职业进阶的要点要领


##### <a name="9">64. 最小路径和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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

###### <a name="10">64. 最小路径和感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
##### <a name="11">62.不同路径</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[62.不同路径](https://leetcode-cn.com/problems/unique-paths/)
```
```
###### <a name="12">62.不同路径感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1.最优子结构：opt[n] = best_of(opt(n-1) , opt(n-2), ...)
2.储存中间状态：opt[i]
3.递推公式（美其名曰：状态转移方程或DP方程）
   Fib：opt[i] = opt[n - 1] + opt[n - 2]
   二维路径：opt[i,j] = opt[i + 1,j] + opt[i,j+1]且判断opt[i,j]是否是空地

```
##### <a name="13">120.三角形最小路径和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
###### <a name="14">分治</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
python add_lrucache
```
```

###### <a name="15">动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="16">53.最大子序列的和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
暴力法+分治发+DP
```
```
##### <a name="17">152.乘积最大子序列</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
```
##### <a name="18">322. 零钱兑换</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
广度优先遍历
DP
```
```
##### <a name="19">198. 打家劫舍</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
###### <a name="20">198. 打家劫舍感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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