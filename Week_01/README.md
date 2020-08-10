```
# 注： 
# 算法训练营 
## 第几周 
### 第几节课
#### 知识点 
1. 细节知识点 
2. ``` 代码 ```
```

[toc]
# 算法训练营
## 第一周
### 第一节课
#### 学习算法的方式
1.不用看书（算法导论也不用看，书和资料在于精不在于多）
   注：看拉布拉多算法总结
2.科学做题：累了消遣娱乐活动 （将抖音时间和娱乐时间换成刷题，但是正经做题的时候不行啊）-> 刷简单（捏软柿子）
   注：消遣和娱乐都做算法
   
#### 软件
1.scapple
2.mindnode
3.百度脑图
#### 知识点 
1.大牛眼里那些类似九九乘法表
2.斐波拉契数、卡特兰数、杨辉三角
3.着重于python和Java
4.链表的时间复杂度
  prepend o(1)
  append o(1)
  lookup o(n)
  insert o(1)
  delete o(1)
  数组的时间复杂度
  prepend o(n)
  append o(1)
  lookup o(1)
  insert o(n)
  delete o(n)


#### 涉及到的算法题
1.删除排序数组中的重复项
2.盛最多水的容器
3.N叉树的前序遍历
4.二叉树的前序遍历
5.[递归代码模版](https://shimo.im/docs/EICAr9lRPUIPHxsH/read)
6.二叉树的最大深度
7.验证二叉搜索树
8.leetcode 146 LRU缓存机制
#### 代码 
##### 爬楼梯
```
1.爬楼梯
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
```
##### LRUCatch
     
   
   
