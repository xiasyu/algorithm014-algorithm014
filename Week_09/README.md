<a name="index">**Index**</a>
<a href="#0">第九周</a>  
&emsp;&emsp;&emsp;<a href="#1">代码 </a>  
&emsp;&emsp;&emsp;&emsp;<a href="#2">72. 编辑距离 记住那张图</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#3">72. 编辑距离 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#4">746. 使用最小花费爬楼梯</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#5">746. 使用最小花费爬楼梯 感想</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#6">746. 使用最小花费爬楼梯 感想 </a>  
&emsp;&emsp;&emsp;&emsp;<a href="#7">300. 最长上升子序列 (动态规划)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#8">300. 最长上升子序列（动态规划） 感想 </a>  
&emsp;&emsp;&emsp;&emsp;<a href="#9">300. 最长上升子序列 (贪心 + 二分)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#10">300. 最长上升子序列 (贪心 + 二分) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#11">91. 解码方法</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#12">91. 解码方法 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#13">32. 最长有效括号（暴力解法）</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#14">32. 最长有效括号 （暴力解法） 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#15">32. 最长有效括号(动态规划解法)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#16">32. 最长有效括号(动态规划解法) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#17">32. 最长有效括号(栈的解法)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#18">32. 最长有效括号(栈的解法) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#19">32. 最长有效括号(正向逆向结合）的解法</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#20">32. 最长有效括号(正向逆向结合的解法)感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#21">84. 柱状图中最大的矩形(暴力解法)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#22">84. 柱状图中最大的矩形(暴力解法) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#23">84. 柱状图中最大的矩形(单调栈解法)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#24">84. 柱状图中最大的矩形(单调栈解法) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#25">85. 最大矩形（单调栈解法）</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#26">85. 最大矩形（单调栈解法）感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#27">85. 最大矩形（动态规划解法）</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#28">85. 最大矩形（动态规划解法） 感想</a>  

# <a name="0">第九周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
#### <a name="1">代码 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)|1|2|
|[746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)|1|2|
|[300. 最长上升子序列(动态规划)](https://leetcode-cn.com/problems/longest-increasing-subsequence/)|1|2|
|[300. 最长上升子序列(贪心 + 二分查找)](https://leetcode-cn.com/problems/longest-increasing-subsequence/)|1|2|
|[91. 解码方法](https://leetcode-cn.com/problems/decode-ways/)|1|2|
|[32. 最长有效括号(暴力解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|2|
|[32. 最长有效括号(动态规划解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|2|
|[32. 最长有效括号(栈的解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|2|
|[32. 最长有效括号(正向逆向结合的解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|2|
|[84. 柱状图中最大的矩形(暴力解法)](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)|1|2|
|[84. 柱状图中最大的矩形(单调栈解法)](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)|1|2|
|[85. 最大矩形(单调栈解法)](https://leetcode-cn.com/problems/maximal-rectangle/)|1|2|





##### <a name="2">72. 编辑距离 记住那张图</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)
```
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
```

###### <a name="3">72. 编辑距离 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/)
```
动态规划：
dp[i][j]代表word1 到i位置转换成word2到j位置需要最少步数
所以
当word1[i] == word2[j]时，dp[i][j] = dp[i-1][j-1]
当word1[i] != word2[j]时，dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
其中dp[i-1][j-1] 代表替换操作 dp[i][j-1]代表插入操作，dp[i-1][j]代表删除操作
   
```
![](media/16031743972700/16031748437652.jpg)


##### <a name="4">746. 使用最小花费爬楼梯</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)
```
    方法一
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
        return min(dp[-1] , dp[-2])  
    方法 二
    def minCostClimbingStairs(self, cost: List[int]) -> int:
         首先得到最有状态转移方程
        n = len(cost)
        dp = [0] * n
        dp[1] = min(cost[0],cost[1])
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i],dp[i - 2] + cost[i - 1])
        return dp[n-1]      
          
```

###### <a name="5">746. 使用最小花费爬楼梯 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode.com/problems/min-cost-climbing-stairs/discuss/657490/Python-solution-from-a-beginner-(some-easy-steps-to-follow-to-solve-dp))
```
再次回顾做过的原代码，发现，我之前想的根本不对
这次重新回顾，并思考重写感悟
跟第二种方式的不同之处在于，我先拿到到达dp[i]的最小花费，然后min(dp[i-1],dp[i]) 求最小值。因为这两个都可以到达顶部
1、从两个方向出发
   到达顶部 min(dp[i] dp[i - 1])
      1.分解dp[i]
        dp[i] = dp[i - 1] + cost[i]
    or  dp[i] = dp[i - 2] + cost[i]
    so. dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
       2.dp[0] = cost[0]
         dp[1] = min(cost[1], cost[0])
2、执行循环即可
3、返回 min(dp[-1],dp[-2])
疑惑：为什么到达dp[i]的最小值，dp[i-1]中的数值也是到达 dp[i - 1]的最小值吗？是！ 原因：前面都是按照min筛选的。暂时这样记住吧。           
  
```

###### <a name="6">746. 使用最小花费爬楼梯 感想 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/yi-bu-yi-bu-tui-dao-dong-tai-gui-hua-de-duo-chong-/)
```
再次回顾这个题，让我感觉到了，做题不要求快，做100道题，最后一道也记不住，甚至回头再看跟新题一样，得不偿失
这道题我有了新的理解
首先是从后往前推（为什么呢？暂时不知道）
   1.到达或者越过第i阶梯都是正确的
      1> 到达第i阶梯，mincost[i] = mincost[i - 1] + cost[i]
      2>  越过第i阶梯(换句话说，只要到达 i- 1阶梯即可)：mincost[i] = mincost[i - 2] + cost[i - 1]
   2.由此可得：minconst[i] = min(mincost[i - 1] + cost[i], mincost[i - 2] + cost[i - 1])
   3.这是从第2阶梯开始看的，所以第0阶梯和第1阶梯还需要我们自己来算，也就是需要显得出cost[0],cost[1]
   代码如下：
   由minconst[i] = min(mincost[i - 1] + cost[i], mincost[i - 2] + cost[i - 1])可得:
   cost[0] = min(cost[0],cost[-1]) = 0
   cost[1] = min(cost[1],cost[0])
   为什么得出这种结果呢：因为min(mincost[i - 1] + cost[i], mincost[i - 2] + cost[i - 1])中，当i= 0的时候，mincost[i - 1] + cost[i] 就是cost[0],mincost[i - 2] + cost[i - 1]就是cost[-1]
   懂了吗？
    
```


##### <a name="7">300. 最长上升子序列 (动态规划)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[300. 最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
```
    时间复杂度为 0(n^2)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
        return min(dp[-1] , dp[-2]) 
        
    方法二：这个方法没有看明白
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size   
```

###### <a name="8">300. 最长上升子序列（动态规划） 感想 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/)
[视频参考链接](https://www.bilibili.com/video/BV137411B7BN?from=search&seid=14029252552532980305)
```
再次回顾，又有不同的感受，感觉之间的做法就形式比着题解抄了一遍。什么玩意儿
1、这道题嵌套了两层for循环，就是将 第i个元素跟他之前的元素进行一一对比，累计第i个元素的最大子序列个数
   dp = [1] * n

   for i in range(len(nums)):
        fof j in range(i):
            核心代码:
            if nums[j] < num[i]:
               dp类似于暂存状态，随着i和j元素的对比，dp[i]不断修改的过程
               dp[i] = max(dp[i],dp[j] + 1)
2. 取dp的最大值即可。（千万不要误以为这是累加的过程，有可能dp[-1]不是最大元素。因为这道题中逻辑上dp没有顺序）
```

##### <a name="9">300. 最长上升子序列 (贪心 + 二分)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        length = 0
        tail = {}
        for i in range(n):
            x = nums[i]
            l = 0
            r = length
            while(l < r):
                mid = (l + r + 1) // 2
                if tail[mid] < x:
                    l = mid
                else:
                    r = mid - 1
            tail[l + 1] = x
            length = max(length, l + 1)
        return length
```
###### <a name="10">300. 最长上升子序列 (贪心 + 二分) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://www.bilibili.com/video/BV1GA411B76a?from=search&seid=14029252552532980305)
```
这个方法有些巧妙
核心思想是：看这个视频吧，好好看！
```

##### <a name="11">91. 解码方法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
from typing import List
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if s[0] == '0':
            return 0
        dp = [0] * (n + 1)
        for i in  range(1, n + 1):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[-1]
```

###### <a name="12">91. 解码方法 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
换了一种解法
关于为什么 dp[0] = 1,dp[1] = 1 
没理解，
```
##### <a name="13">32. 最长有效括号（暴力解法）</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
from typing import List
class Solution:
     暴力解法
    def longestValidParentheses(self, s: str) -> int:
         首先定义一个 isValid的函数，判断字串是否是合法字串
         然后截取测试长度的字串，进行判断。如果截取的字串为有效字串，则长度为合法字串（由长到短开始截取）

         定义的判断字串是否合法的函数
        def isValid(subs):
            stack = []
            n = len(subs)
            for i in range(n):
                if subs[i] == '(':
                    stack.append('(')
                elif stack != [] and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []

         开始进行遍历
        n = len(s)
        if n < 2:
            return 0
        因为有效字串一定是偶数，如果总长度为偶数，则边界n否则为n-1。每次遍历都减去两个长度。
        for i in range(n if n % 2 == 0 else n - 1, 0 , -2):
            for j in range(n - i + 1):
                if isValid(s[j:j+i]):
                    return i
        return 0
```

###### <a name="14">32. 最长有效括号 （暴力解法） 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
``` 
1、暴力解法利用了栈的原理，来判断字符串的合法性
2、利用了合法的字符串为偶数的原理来从长到短遍历字符串
   1.首先找到最大偶数
   2.在最大偶数中每次--2
   3.每次验证合法性
   4.合法即返回
```

##### <a name="15">32. 最长有效括号(动态规划解法)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
第二种动态规划的方法
    def longestValidParentheses1(self, s: str) -> int:
         首先找到状态转移方程
         dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i-1] - 2]
        return max(dp)
```
###### <a name="16">32. 最长有效括号(动态规划解法) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/)
```
其实视频里讲的已经很详细了
思路
首先，只有')'才会更新状态数字。'('对应的状态数字都为0.
1、首先找到状态转移方程。
   dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
   解释一下这个方程的意思
   1.2 代表的是，如果i')'找到了配对儿的'(',则程度为2，这个2就是自己的2
   2.dp[i - 1]代表的是第i个有效配对儿的'()'中间的合法字符传长度
   3.dp[i - dp[i - 1] - 2] 是与第i个')'配对的'('的上一个dp存储的长度。
   结合视频详细观看
   
 2、对于中间出现的不合法字符串：
    1.如果是中间多了个'(',不用管哦，因为它对应的状态数字就是0
    2.如果是中间多了个')',直接计算就好了，上面的状态转移方程求出对应的状态为0
       

```

##### <a name="17">32. 最长有效括号(栈的解法)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
 第三种方法 栈
    def longestValidParentheses3(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        stack = [-1]
        max_length = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(length, max_length)
        return max_length
```
###### <a name="18">32. 最长有效括号(栈的解法) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
时间复杂度为 o(n)
首先在栈内添加 -1
1、遇到'('则入栈，遇到')'则出栈
2、入栈不做操作，出栈的时候：
   1.如果栈不为空，
   2.如果栈为空，则将i入栈
   3.计算 i - stack[-1],得到的长度跟max_length对比，取大者
3、返回max_length   
```

##### <a name="19">32. 最长有效括号(正向逆向结合）的解法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
 第四种方法 正向逆向结合法
    def longestValidParentheses4(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * right)
            elif left < right:
                left = right = 0

        left = right = 0
        
        for c in s[::-1]:
            if c == ')':
                right += 1
            else:
                left += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0   
        return max_length
```
###### <a name="20">32. 最长有效括号(正向逆向结合的解法)感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
正向逆向结合的思路
1、正向开始，
   1.遇到'(' +1，遇到')' +1,当两个值相等的时候，max_length为 max(max_length,2 * left) 
   2.如果出现了')'的个数大于'(',则将')'和'('的个数置为0.
   遍历结束得到 max_length
2.逆向开始
   注意：跟正向不同的是
   1.字符串倒置
   1. 如果出现了'('的个数大于')',则将')'和'('的个数置为0. 
返回 max(max_length_left, max_length_right)
```
##### <a name="21">84. 柱状图中最大的矩形(暴力解法)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[84. 柱状图中最大的矩形(暴力解法)](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
```
from typing import List
class Solution:
     第一种方式 (暴力解法)
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            left = i
            right = i
            height = heights[i]
            这一步我在判断heights[left - 1] >= height的时候出错了，>= 我写成了 <,这是不对的。因为只有在大于height的时候left才会想做移动，right同理
            while left - 1 >= 0 and heights[left - 1] >= height:
                left -= 1
            while right + 1 < n and heights[right + 1] >= height:
                right += 1
            max_area = max(max_area, height * (right - left + 1))
        return max_area
```

###### <a name="22">84. 柱状图中最大的矩形(暴力解法) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
时间复杂度为 o(n^2), 空间复杂度为 o(1)
暴力解法其实就是固定高度，移动宽度的解法
1、第i个矩形高度不动，来找是当前面积最大的宽度
2、for循环柱子
   1.以当前柱子为准，左右移动坐标，如果left >= height[i],left--。如果right >= height[i],right ++
   2.记录每次的最大面积 max_area = max(max_area, height * (right - left + 1))
 return max_area   

```
##### <a name="23">84. 柱状图中最大的矩形(单调栈解法)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
 第二种方式 （单调栈）
    def largestRectangleArea1(self, heights: List[int]) -> int:
         首尾添加0高度的柱子
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for idx_right in range(len(heights)):
            while stack and heights[stack[-1]] > heights[idx_right]:
                h_mid = heights[stack.pop()]
                idx_left = stack[-1]
                一定要记住这个边界问题 idx_right - idx_left - 1
                res = max(res, h_mid * (idx_right - idx_left - 1))
            stack.append(idx_right)
        return res
```

###### <a name="24">84. 柱状图中最大的矩形(单调栈解法) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
首先要在首位各自添加一个0元素，为了进行边界判断使用。因为原始数组中最左侧的元素没有左边界，最右侧的元素没有有边界
关键点：向左向右找次小元素，正好符合单调栈的模式
初始化一个栈 stack
1、如果栈不为空，并且栈顶元素大于接下来的第i个元素，则弹出栈顶元素，拿到高度。
   1.拿到栈顶元素的高度后，pop出栈顶元素定义为h_mid，然后取出stack[-1]定义为idx_left(pop出去的栈顶元素的前一个值),stack[-1]其实也是pop出去的栈顶元素的左边界
    2.max_area = max(max_area,h_mid * (i - idx_left - 1))
2、如果条件一一直成立，则一直执行条件一，否则
    1.结束条件一，将i入栈
return max_area

```
##### <a name="25">85. 最大矩形（单调栈解法）</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)
```
from typing import List
class Solution:
     单调栈 解法（嵌套了 84 求最大矩形面积 的完整代码）
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        max_area = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

     计算矩形的最大面积
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        max_area = 0
        stack = []
        for idx_right in range(len(heights)):
            while stack and heights[stack[-1]] > heights[idx_right]:
                h_mid = heights[stack.pop()]
                idx_left = stack[-1]
                max_area = max(max_area, h_mid * (idx_right - idx_left - 1))
            stack.append(idx_right)
        return max_area
```
###### <a name="26">85. 最大矩形（单调栈解法）感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
其实是借用了 84题的完整代码
1、循环矩阵的每一层,初始化存储当前层高度的数组heights
2、每到一层，将上层的数值叠加
   1.如果matrix[i][j] == 0，则重置heights[j]高度为0
   2.否则进行 heights[j] += 1
   3.叠加完成，将heights传入到最大矩形面积的方法中，max(max_area, self.largestRectangleArea(heights))
retrun max_area    
```
##### <a name="27">85. 最大矩形（动态规划解法）</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
    m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                row_with = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                for k in range(i, -1, -1):
                    row_with = min(row_with,dp[k][j])
                    max_area = max(max_area,row_with * (i - k + 1))
        return max_area
```

###### <a name="28">85. 最大矩形（动态规划解法） 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/)
```
要理解此方法，首先要先理解暴力破解法
暴力破解法描述：
1.首先我们计算出当前着这一行矩形的最大宽度，我们可以通过计算每一行每一个方块儿连续1的数量之和来实现这一点。每遍历完一行就更新该点的最大可能宽度。
   代码：row[i] = row[i - 1] + i if row[i] == '1'
2.同时我们在计算宽度的过程中，也执行着这个操作
   1.当前行往上遍历。但是这个遍历的过程我们取的是已经记录在dp中的最小值，就是当前行，当前列所能计算矩形面积的最大宽度。如果没理解，看官方吧😢
3.不断更新max_area   

```
