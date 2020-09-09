<a name="index">**Index**</a>
&emsp;<a href="#0">第四周</a>  
&emsp;<a href="#1">贪心算法：</a>  
&emsp;<a href="#2">动态规划</a>  
&emsp;<a href="#3">贪心算法和动态规划</a>  
&emsp;<a href="#4">回溯的知识点：(讲的很好)</a>  
&emsp;<a href="#5">剪枝</a>  
&emsp;<a href="#6">图的最短路径</a>  
&emsp;<a href="#7">DFS 代码递归写法</a>  
&emsp;<a href="#8">DFS 代码非递归写法</a>  
&emsp;<a href="#9">二分查找的代码模版(非递归)</a>  
&emsp;<a href="#10">二分查找的代码模版(递归)</a>  
&emsp;<a href="#11">题型二：Flood Fill</a>  
&emsp;<a href="#12">题型三：字符串中的回溯问题</a>  
&emsp;<a href="#13">题型四：游戏问题</a>  
&emsp;&emsp;&emsp;<a href="#14">代码</a>  
&emsp;&emsp;&emsp;<a href="#15">102. 二叉树的层序遍历</a>  
&emsp;&emsp;&emsp;<a href="#16">33. 搜索旋转排序数组</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#17"> 搜索旋转排序数组的感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#18">22. 括号生成</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#19">全排列感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#20">47. 全排列 II</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#21">全排列 II感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#22">77. 组合</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#23">组合感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#24">560. 和为K的子数组</a>  
## <a name="0">第四周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

## <a name="1">贪心算法：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的结果
## <a name="2">动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：
## <a name="3">贪心算法和动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
区别：贪心算法对每个子问题的解决方案都作出选择，不能回退。动态规划则会保寸以前的结果，并根据以前的结果对当前结果进行选择，有回退功能。
## <a name="4">回溯的知识点：(讲的很好)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
> https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

 
## <a name="5">剪枝</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

## <a name="6">图的最短路径</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
使用广度优先搜索



## <a name="7">DFS 代码递归写法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

```
visited = set()
def dfs(self, node:TreeNode ,visited:List()):
    if node is in visited():
        // already visited
        return
        
    visited.append(node.value)
    // process current node here
    ...
    for next_node in node.children():
        if next_mode is not in visited:
            self.dfs(next_node, visited)
```
## <a name="8">DFS 代码非递归写法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```

```

## <a name="9">二分查找的代码模版(非递归)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
def binarySearch(self, nums: List[int], target: int) -> int:
    left,right = 0, n - 1
    while left < right:
           mid = (right + left) // 2
           if nums[mid] < target:
              right = mid - 1
           elif num[mid] > target:
              left = mid + 1
            else:
               return mid
                      
              
```
## <a name="10">二分查找的代码模版(递归)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
def binarySearch(self, nums: List[int], target: int) -> int:
    return self.binarySearchHelper(nums,target,0,n - 1,(n - 1) // 2)
    
    
def binarySearchHelper(self, nums: List[int], target: int,left: int, right: int, mid: int) -> int:   
     // recurison terminal
     if nums[mid] == target:
         retrun mid
    
    // process current logic
    mid = (left + right) // 2
    if nums[mid] < target
        right = mid - 1
    else nums[mid] > target
        left = mid + 1    
    // dill down
    self.binarySearchHelper(nums,target,left,right,mid)
    // restore status 
      
```

##题型一：排列、组合、子集相关问题
提示：这部分练习可以帮助我们熟悉「回溯算法」的一些概念和通用的解题思路。解题的步骤是：先画图，再编码。去思考可以剪枝的条件， 为什么有的时候用 used 数组，有的时候设置搜索起点 begin 变量，理解状态变量设计的想法。

46. 全排列（中等）
47. 全排列 II（中等）：思考为什么造成了重复，如何在搜索之前就判断这一支会产生重复；
39. 组合总和（中等）
40. 组合总和 II（中等）
77. 组合（中等）
78. 子集（中等）
90. 子集 II（中等）：剪枝技巧同 47 题、39 题、40 题；
60. 第 k 个排列（中等）：利用了剪枝的思想，减去了大量枝叶，直接来到需要的叶子结点；
93. 复原 IP 地址（中等）
## <a name="11">题型二：Flood Fill</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
提示：Flood 是「洪水」的意思，Flood Fill 直译是「泛洪填充」的意思，体现了洪水能够从一点开始，迅速填满当前位置附近的地势低的区域。类似的应用还有：PS 软件中的「点一下把这一片区域的颜色都替换掉」，扫雷游戏「点一下打开一大片没有雷的区域」。

下面这几个问题，思想不难，但是初学的时候代码很不容易写对，并且也很难调试。我们的建议是多写几遍，忘记了就再写一次，参考规范的编写实现（设置 visited 数组，设置方向数组，抽取私有方法），把代码写对。

733. 图像渲染（Flood Fill，中等）
200. 岛屿数量（中等）
130. 被围绕的区域（中等）
79. 单词搜索（中等）
说明：以上问题都不建议修改输入数据，设置 visited 数组是标准的做法。可能会遇到参数很多，是不是都可以写成成员变量的问题，面试中拿不准的记得问一下面试官

## <a name="12">题型三：字符串中的回溯问题</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
提示：字符串的问题的特殊之处在于，字符串的拼接生成新对象，因此在这一类问题上没有显示「回溯」的过程，但是如果使用 StringBuilder 拼接字符串就另当别论。
在这里把它们单独作为一个题型，是希望朋友们能够注意到这个非常细节的地方。

1. 电话号码的字母组合（中等），题解；
2. 字母大小写全排列（中等）；
3. 括号生成（中等） ：这道题广度优先遍历也很好写，可以通过这个问题理解一下为什么回溯算法都是深度优先遍历，并且都用递归来写。

## <a name="13">题型四：游戏问题</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
回溯算法是早期简单的人工智能，有些教程把回溯叫做暴力搜索，但回溯没有那么暴力，回溯是有方向地搜索。「力扣」上有一些简单的游戏类问题，解决它们有一定的难度，大家可以尝试一下。

51. N 皇后（困难）：其实就是全排列问题，注意设计清楚状态变量，在遍历的时候需要记住一些信息，空间换时间；
37. 解数独（困难）：思路同「N 皇后问题」；
488. 祖玛游戏（困难）
529. 扫雷游戏（困难）



#### <a name="14">代码</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)|1|1|
|[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)|1|1|
|[22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)|1|1|
|[46. 全排列](https://leetcode-cn.com/problems/permutations/)|1|1|
|[47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)|1|1|

#### <a name="15">102. 二叉树的层序遍历</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
```
class TreeNode:
    def __init__(self, x:int):
        self.val = x;
        self.left = None
        self.right = None

from typing import List
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level = []
        queue = collections.deque()
        queue.append(root)
        dummy = TreeNode(-1)
        queue.append(dummy)

        while len(queue) != 0:
            node = queue.popleft()
            if node == dummy:
                res.append(level)
                level = []
                if len(queue) != 0:
                    queue.append(dummy)
            else:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

      层序遍历
     def levelOrder(self, root: TreeNode) -> List[List[int]]:
    
         res = []
         self.levelOrderHelper(root,0,res)
         return res
    
     def levelOrderHelper(self, node: TreeNode, level: int, res: List[int]):
         if len(res) == level:
             res.append([])
         res[level].append(node.val)
    
         if node.left:
             self.levelOrderHelper(node.left,level + 1,res)
         if node.right:
             self.levelOrderHelper(node.right, level + 1, res)

     前中序创建二叉树
    def buildTree(self, preorder:List[int], inorder:List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        if len(preorder) != len(inorder):
            return None

        n = len(preorder)

        dict = {}
        for i in range(n):
            dict[inorder[i]] = i
        return self.buildTreeHelper(preorder,0,n - 1, 0, n - 1,dict)

     创建二叉树帮助
    def buildTreeHelper(self,preorder:List[int], pre_left: int, pre_right: int, in_left: int, in_right: int, dict: {}) -> TreeNode:

        if pre_left > pre_right or in_left > in_right:
            return None

        rootValue = preorder[pre_left]
        index_root = dict[rootValue]
        root = TreeNode(rootValue)

        root.left = self.buildTreeHelper(preorder,pre_left + 1,index_root - in_left + pre_left, in_left, index_root - 1,dict)
        root.right = self.buildTreeHelper(preorder, index_root - in_left + pre_left + 1, pre_right, index_root + 1, in_right,
                                         dict)
        return root

a = Solution()
root = a.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(a.levelOrder(root))


```
####### 二叉树层序遍历的感想
```

    
```

#### <a name="16">33. 搜索旋转排序数组</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
```
from typing import List
class Solution:
第一种方式：
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] < nums[0]:
                    nums[mid] = float("inf")
            else:
                if nums[mid] >= nums[0]:
                    nums[mid] = float("-inf")

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
  第二种方式
  def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return  -1
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1              

```
##### <a name="17"> 搜索旋转排序数组的感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
第一种方式：
    
第二种方式
    
  

```
##### <a name="18">22. 括号生成</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
```
    深度优先遍历
    class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0,0,n,"",res)
        return res

    def dfs(self, left:int, right:int, n:int, s:str, res:List[str]):

         recusion termimal
        if left == n and right == n:
            res.append(s)

         process current logic

         dill down
        if left < n:
            self.dfs(left + 1, right, n, s + "(", res)

        if right < left and right < n:
            self.dfs(left, right + 1, n, s + ")", res)

         restore

     广度优先遍历 （没成功）
         def bfs(self, n:int, res:List[str]) -> List[str]:
        root = ListNode("",n,n)
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:

            node = queue.popleft()
            if node.left == 0 and node.right == 0:
                res.append(node.s)

            if node.left > 0:
                listNode = ListNode(node.s + "(",node.left - 1,node.right)
                queue.append(listNode)

            if node.right > node.left and node.right > 0:
                listNode = ListNode(node.s + ")",node.left,node.right - 1)
                queue.append(listNode)
     
```
#####46. 全排列
时间复杂度为 o(n * n!)
[46. 全排列](https://leetcode-cn.com/problems/permutations/)
```
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 0:
            return []
        used = [False] * n
        res = []
        path = []
        self.dfs(nums, n,0,used,res,path)
        return res

    def dfs(self, nums:List[int], n:int, depth:int, used:List[bool],res:List[List[int]],path:List[int]):
        if n == depth:
            res.append(path.copy())
            return res
        for i in range(n):
            if used[i] == False:
                path.append(nums[i])
                used[i] = True
                self.dfs(nums,n,depth + 1,used,res,path)
                used[i] = False
                path.pop()
a = Solution()
print(a.permute([1,2,3]))
```
###### <a name="19">全排列感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
注意：最终的执行方式还是递归，脑补递归的画面，一层一层往下走，直到给你一个信号 return，就开始一层一层往上返回，每层返回都会执行完整个函数题
其实递归的过程跟上一个执行方法无关，是开辟了一个新的栈空间，一层递归一个新的栈空间。只有最后的栈空间调用结束，才会一层一层返回😄
```
##### <a name="20">47. 全排列 II</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[47. 全排列 II](https://leetcode-cn.com/problems/permutations-ii/)
```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 0:
            return []
        used = [False] * n
        path = []
        res = []
        nums.sort() // 排序
        self.dfs(nums, n, 0, res, used, path)
        return res

    def dfs(self, nums: List[int], n:int, depth:int, res:List[int], used:List[bool], path:List[int]):
        if depth == n:
            res.append(path.copy())
        for i in range(n):
            if used[i] == True:
                continue
            if (i > 0) and (nums[i] == nums[i - 1]) and (not used[i - 1]) : // 此处一定是 used[i - 1],代表前一个元素已经被使用过
                continue
            path.append(nums[i])
            used[i] = True
            self.dfs(nums, n, depth + 1, res, used, path)
            used[i] = False
            path.pop()         
```
###### <a name="21">全排列 II感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
注意：
剪枝剪去的是：跟前一个极点相同，并且前一个结点已经访问过，此时这个结点就不再访问，因为会跟之前的结点产生的叶子重复
```
##### <a name="22">77. 组合</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k > n:
            return []
        res = []
        path = []
        self.dfs(n, k, 0, res, path, 1)
        return res

    def dfs(self, n:int, k:int, depth:int, res:{}, path:List[int],begin:int):
        if depth == k:
            res.append(path.copy())
            return
        for i in range(begin,n + 1):
            path.append(i)
            self.dfs(n, k, depth + 1, res, path, i + 1)
            path.pop()
```
###### <a name="23">组合感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
注意：此处不使用used[bool]是因为begin已经排除了重复访问的可能

```

##### <a name="24">560. 和为K的子数组</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i , -1, -1 ):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count 
        
 def subarraySum(self, nums: List[int], k: int) -> int:

        pre = 0
        dict = {pre:1}
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            target = pre - k
            if target in dict.keys():
                count += dict[target]
                
            if pre in dict.keys():
                dict[pre] = dict[pre] + 1
            else:
                dict[pre] = 1
        return count

```


