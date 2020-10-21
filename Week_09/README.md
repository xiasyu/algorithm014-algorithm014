<a name="index">**Index**</a>
<a href="#0">第九周</a>  
&emsp;&emsp;&emsp;<a href="#1">代码 </a>  
&emsp;&emsp;&emsp;&emsp;<a href="#2">72. 编辑距离</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#3">72. 编辑距离 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#4">746. 使用最小花费爬楼梯</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#5">746. 使用最小花费爬楼梯 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#6">300. 最长上升子序列</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#7">300. 最长上升子序列感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#8">32. 最长有效括号(动态规划解法)</a>  
<a href="#9">      # 首先找到状态转移方程</a>  
<a href="#10">      # dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#11">32. 最长有效括号(动态规划解法) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#12">32. 最长有效括号(栈的解法)</a>  
<a href="#13">第三种方法 栈</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#14">32. 最长有效括号(栈的解法) 感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#15">32. 最长有效括号(正向逆向结合的解法</a>  
<a href="#16">第四种方法 正向逆向结合法</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#17">32. 最长有效括号(正向逆向结合的解法)感想</a>  

# <a name="0">第九周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
#### <a name="1">代码 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)|1|1|
|[746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)|1|1|
|[300. 最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)|1|1|
|[91. 解码方法](https://leetcode-cn.com/problems/decode-ways/)|1|1|
|[32. 最长有效括号(暴力解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|1|
|[32. 最长有效括号(动态规划解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|1|
|[32. 最长有效括号(栈的解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|1|
|[32. 最长有效括号(正向逆向结合的解法)](https://leetcode-cn.com/problems/longest-valid-parentheses/)|1|1|



##### <a name="2">72. 编辑距离</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
```

###### <a name="5">746. 使用最小花费爬楼梯 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode.com/problems/min-cost-climbing-stairs/discuss/657490/Python-solution-from-a-beginner-(some-easy-steps-to-follow-to-solve-dp))
```
这个思路大概能想的出来，但是具体到代码层次还需要详细琢磨
1、这是一个动态规划问题
第i阶需要的体力是：
dp[i] = cost[i] + min(dp[i-1],dp[i-2])
最后返回
min(dp[i-1],dp[i-2])

```


##### <a name="6">300. 最长上升子序列</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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

###### <a name="7">300. 最长上升子序列感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[参考链接](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
```
第一种方法：
i > j
1、建立数组长度的dp数组，存储为[1,1...]

2、两两比较，只要发现num[i]大于num[j]，则dp[i] = max(dp[j] + 1, dp[i])

3、输出dp中的最大值 max(dp)即可
   
```
#####91. 解码方法
```
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
```

######91. 解码方法 感想
```
没能太理解
```
#####32. 最长有效括号（暴力解法）
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

######32. 最长有效括号 （暴力解法） 感想
``` 
1、暴力解法利用了栈的原理，来判断字符串的合法性
2、利用了合法的字符串为偶数的原理来从长到短遍历字符串
   1.首先找到最大偶数
   2.在最大偶数中每次--2
   3.每次验证合法性
   4.合法即返回
```

##### <a name="8">32. 最长有效括号(动态规划解法)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
#第二种动态规划的方法
    def longestValidParentheses1(self, s: str) -> int:
        # <a name="9">首先找到状态转移方程</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        # <a name="10">dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i-1] - 2]
        return max(dp)
```
###### <a name="11">32. 最长有效括号(动态规划解法) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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

##### <a name="12">32. 最长有效括号(栈的解法)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
# <a name="13">第三种方法 栈</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
###### <a name="14">32. 最长有效括号(栈的解法) 感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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

##### <a name="15">32. 最长有效括号(正向逆向结合的解法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
# <a name="16">第四种方法 正向逆向结合法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
    def longestValidParentheses4(self, s: str) -> int:
        def lengthIndifferent(s, fromLeft) -> int:
            max_length = 0
            left_num = 0
            right_num = 0
            if fromLeft == True:
                for c in s:
                    if c == '(':
                        left_num += 1
                    else:
                        right_num += 1
                    if left_num == right_num:
                        max_length = max(max_length, 2 * left_num)

                    elif right_num > left_num:
                        right_num = left_num = 0
            if fromLeft == False:
                for c in s[::-1]:
                    if c == '(':
                        left_num += 1
                    else:
                        right_num += 1
                    if left_num == right_num:
                        max_length = max(max_length,2 * left_num)
                    elif right_num < left_num:
                        right_num = left_num = 0
            return max_length


        max_from_left = lengthIndifferent(s,True)
        max_from_right = lengthIndifferent(s,False)

        return max(max_from_left,max_from_right)
```
###### <a name="17">32. 最长有效括号(正向逆向结合的解法)感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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


