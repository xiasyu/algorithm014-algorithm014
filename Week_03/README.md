<a name="index">**Index**</a>
&emsp;<a href="#0">算法第三周</a>  
&emsp;<a href="#1">感想</a>  
&emsp;<a href="#2">分治的思想</a>  
&emsp;<a href="#3">回溯的模版</a>  
&emsp;<a href="#4">图示</a>  
&emsp;&emsp;&emsp;<a href="#5">代码</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#6">剑指 Offer 40. 最小的k个数</a>  
<a href="#7">          # dill down</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#8">49. 字母异位词分组</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#9">剑指 Offer 05. 替换空格</a>  
<a href="#10">      # s = '20%'.join(s.split(' '))</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#11">剑指 Offer 68 - II. 二叉树的最近公共祖先</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#12">15. 三数之和</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#13">18. 四数之和</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#14">1498. 满足条件的子序列数目</a>  
## <a name="0">算法第三周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="1">感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1、多练多看多理解
2、实在看不懂的就背下来

```
## <a name="2">分治的思想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1. terminator
2. process(split your big problem)
3. drill down(subproblems)
4. merge(subsult
5. reverse status
```
## <a name="3">回溯的模版</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
res = []
state = []
p,q,r
def backtrack(状态，条件1，条件2，...):
    if 不满足合法条件（可以说剪枝）
        return
    elif 状态满足最终要求
        res.append(state) 加入结果
        return
    主要递归过程，一般带有循环体，或者条件体
    for 满足执行条件
    if 满足执行条件
       backtrack(状态，条件1，条件2，...)
backtrack(状态，条件1，条件2，...)      
return res 
```
## <a name="4">图示</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
![-w1413](media/15982561375067/15986786913919.jpg)


#### <a name="5">代码</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)|1|1|
|[49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)|1|1|
|[剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof)|1|1|
|[剑指 Offer 06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof)|1|1|
|[剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)|1|1|
|[15. 三数之和](https://leetcode-cn.com/problems/3sum/) |1|map方法不对，有重复|
|[18. 四数之和](https://leetcode-cn.com/problems/4sum/)|1|1|
|[1498. 满足条件的子序列数目](https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)|1|1|
|[77. 组合](https://leetcode-cn.com/problems/combinations/)|1|1|
|[46. 全排列](https://leetcode-cn.com/problems/permutations/)|1|1|
|[105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|1|1|

|判断搜索二叉树|||





##### <a name="6">剑指 Offer 40. 最小的k个数</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)
```
 参考链接 https://www.bilibili.com/video/BV1Eb41147dK?from=search&seid=10277900355091596982
from typing import List
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

         系统堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        res = [-x for x in hp]

         自定义堆
         self.heapSort(arr)
         res = arr[:k]
        return res


     堆排序
    def heapSort(self,arr: List[int]):
        self.buildHeap(arr,len(arr))
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i];
            arr[i] = arr[0]
            arr[0] = temp
            self.buildHeap(arr,i)

     生成一个堆
    def buildHeap(self,arr: List[int],n:int):
        lastNode = n - 1
        parent = (lastNode - 1) // 2
        for i in range(parent,-1,-1):
            self.heapify(arr,n,i)

    一开始写的heapify函数是从顶部开始向下的，所以会出现最大数在最底下冒不上来的情况，但是up写的第二个build_heap函数包含了heapify并且是从底层开始的，所以能生成堆
    def heapify(self, arr: List[int], n: int, i: int):
         recursion terminator
        if i >= n:
            return

         procell login in current level
        cr = 2 * i + 2
        tempMax = i
        cl = 2 * i + 1

        if ((cl < n) and (arr[cl] > arr[tempMax])):
            tempMax = cl
        if ((cr < n) and (arr[cr] > arr[tempMax])):
            tempMax = cr
        if tempMax != i:
            temp = arr[tempMax]
            arr[tempMax] = arr[i]
            arr[i] = temp
            # <a name="7">dill down</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
            self.heapify(arr, n, tempMax)

a = Solution()
print(a.getLeastNumbers([4,10,3,5,1,2],4))
```
##### <a name="8">49. 字母异位词分组</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[49. 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)
```
from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        return ans.values()



         ans = collections.defaultdict(list)
         for s in strs:
             count = [0] * 26
             for c in s:
                 count[ord(c) - ord('a')] += 1
             ans[tuple(count)].append(s)
         return ans.values()


a = Solution()
print(a.groupAnagrams(["ate","eat","nta","atn","sdr"]))
```

##### <a name="9">剑指 Offer 05. 替换空格</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof)
```
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.replace(' ','20%')
        # <a name="10">s = '20%'.join(s.split(' '))</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        replaceS = ''
        for idx, val in enumerate(s):
            if val == ' ':
                replaceS += '%20'
            else:
                replaceS += val
        return replaceS
a = Solution()
print(a.replaceSpace("We are happy."))
```
#####剑指 Offer 06. 从尾到头打印链表
[剑指 Offer 06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof)
```

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
     反序遍历
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        self.helper(head, res)
        res = res[::-1]
        return res

    def helper(self, head: ListNode, res: List[int]):
         recursion terminator
        if head == None:
            return res

         process login in current level
        res.append(head.val)

         drill down
        self.helper(head.next, res)

         reverse the current status if needed

     创建链表
    def createListMode(self,nums:List[int]) -> ListNode:
        if len(nums) == 0:
            return None
        tempListNode = ListNode(-1)
        head = ListNode(nums[0])
        tempListNode.next = head
        for i in range(1,len(nums)):
            head.next = ListNode(nums[i])
            head = head.next

        return tempListNode.next
a = Solution()
head = a.createListMode([1,3,2,9,10])
print(head)
print(a.reversePrint(head))

```
##### <a name="11">剑指 Offer 68 - II. 二叉树的最近公共祖先</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)
```
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if left is None:
            return right
        if right is None:
            return left  
```

##### <a name="12">15. 三数之和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[15. 三数之和](https://leetcode-cn.com/problems/3sum/) 
```
    def threeSumMap(self, nums: List[int]) -> List[List[int]]:
        res = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            dict = {}
            for second in range(first + 1, len(nums)):
                if second > first + 2 and nums[second] == nums[second - 1] and nums[second - 1] == nums[second - 2]:
                    continue
                value = target - nums[second]
                if value in dict:
                    res.append([nums[first], value, nums[second]])
                dict[nums[second]] = second
        return res
```

##### <a name="13">18. 四数之和</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[18. 四数之和](https://leetcode-cn.com/problems/4sum/)
```
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in  range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                four = len(nums) - 1
                for three in range(second + 1, len(nums)):
                    if three > second + 1 and nums[three] == nums[three - 1]:
                        continue
                    while three < four and nums[second] + nums[three] + nums[four] + nums[first] > target:
                        four -= 1
                    if three == four:
                        break
                    if nums[second] + nums[three] + nums[four] + nums[first] == target:
                        res.append([nums[first],nums[second],nums[three],nums[four]])
        return res

a = Solution()
print(a.fourSum([1,0,-1,0,-2,2],0))
```
##### <a name="14">1498. 满足条件的子序列数目</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[1498. 满足条件的子序列数目](https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)
```
from typing import List
import bisect
class Solution:
    
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10 ** 9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P


        nums.sort()
        ans = 0
        for i,num in enumerate(nums):
            if 2 * nums[i] > target:
                break
            max = target - nums[i]
            pos = bisect.bisect_right(nums,max) - 1
            contribute = f[pos - i] if pos >= i else 0
            ans += contribute
        return  ans % P

     双指针
    def numSubseqDoublePointer(self, nums: List[int], target: int) -> int:
        n = len(nums)
        P = 10**9 + 7
        f = [1] + [0] * (n - 1)
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % P

        ans = 0
        nums.sort()
        i = 0
        j = n - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                ans = (ans + f[j - i]) % P
                i += 1

        return ans



a = Solution()
print(a.numSubseqDoublePointer([5,2,4,1,7,6,8],16))
```

#####77. 组合
[77. 组合](https://leetcode-cn.com/problems/combinations/)
```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        state = []
        def backtrack(p,state):
            if len(state) == k:
                res.append(state[:])    
            for i in range(p, n + 1):
                state.append(i)
                backtrack(i + 1, state)
                state.pop()
        backtrack(1, state)        
        return res
    
    应用了数学公式    
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n < k or k <= 0:
            return res
        res = self.combine(n -1, k - 1)
        if len(res) == 0:
            res.append([])
        for list in res:
            list.append(n)
        res = res + self.combine(n - 1, k)
        return res        
```

#####46. 全排列
[46. 全排列](https://leetcode-cn.com/problems/permutations/)
```
from typing import List
import collections
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n == 0:
            return res
        path = []
        used = [0] * n
        self.dfs(nums, n, 0, path, used, res)
        return res

    def dfs(self, nums: List[int], n: int, depth:int, path:List[int], used: List[bool], res: List[List[int]]):
        if depth == n:
            res.append(path.copy())
            return ;
        for i in range(n):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.dfs(nums, n, depth + 1, path, used, res)
            path.pop()
            used[i] = False

a = Solution()
print(a.permute([1,2]))
```
