<a name="index">**Index**</a>
&emsp;<a href="#0">第四周</a>  
&emsp;<a href="#1">贪心算法：</a>  
&emsp;<a href="#2">动态规划</a>  
&emsp;<a href="#3">贪心算法和动态规划</a>  
&emsp;<a href="#4">DFS 代码递归写法</a>  
&emsp;<a href="#5">DFS 代码非递归写法</a>  
&emsp;<a href="#6">二分查找的代码模版(非递归)</a>  
&emsp;<a href="#7">二分查找的代码模版(递归)</a>  
&emsp;&emsp;&emsp;<a href="#8">代码</a>  
&emsp;&emsp;&emsp;<a href="#9">102. 二叉树的层序遍历</a>  
&emsp;&emsp;&emsp;<a href="#10">33. 搜索旋转排序数组</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#11"> 搜索旋转排序数组的感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#12">22. 括号生成</a>  
## <a name="0">第四周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

## <a name="1">贪心算法：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的结果
## <a name="2">动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：
## <a name="3">贪心算法和动态规划</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
区别：贪心算法对每个子问题的解决方案都作出选择，不能回退。动态规划则会保寸以前的结果，并根据以前的结果对当前结果进行选择，有回退功能。

## <a name="4">DFS 代码递归写法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

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
## <a name="5">DFS 代码非递归写法</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```

```

## <a name="6">二分查找的代码模版(非递归)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
## <a name="7">二分查找的代码模版(递归)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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

#### <a name="8">代码</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)|1|1|
|[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)|1|1|
|[22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)|1|1|



#### <a name="9">102. 二叉树的层序遍历</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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

#### <a name="10">33. 搜索旋转排序数组</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
##### <a name="11"> 搜索旋转排序数组的感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
第一种方式：
    
第二种方式
    
  

```
##### <a name="12">22. 括号生成</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
        print(0)
        if node.left == 0 and node.right == 0:
            res.append(node.s)
            return res
        if node.left > 0:

            listNode = ListNode(node.s + "(",node.left - 1,node.right)
            queue.append(listNode)
        elif node.right > node.left and node.right > 0:
            listNode = ListNode(node.s + ")",node.left,node.right - 1)
            queue.append(listNode)
     
```


