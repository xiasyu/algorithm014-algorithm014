<a name="index">**Index**</a>
&emsp;<a href="#0">算法训练营第二周</a>  
&emsp;&emsp;<a href="#1">感想</a>  
&emsp;&emsp;<a href="#2">第一节课</a>  
&emsp;&emsp;&emsp;<a href="#3">哈希表概念</a>  
&emsp;&emsp;&emsp;<a href="#4">四件套</a>  
&emsp;&emsp;&emsp;<a href="#5">二叉树</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#6">概念：</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#7">性质：</a>  
&emsp;&emsp;&emsp;<a href="#8">满二叉树</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#9">概念：</a>  
&emsp;&emsp;&emsp;<a href="#10">完全二叉树</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#11">概念：</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#12">性质：</a>  
&emsp;&emsp;&emsp;<a href="#13">二叉树的存储结构</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#14">二叉树的层序遍历</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#15">二叉树的前序遍历</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#16">二叉树的中序遍历</a>  
&emsp;&emsp;&emsp;<a href="#17">二叉搜索树的特点</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#18">线索</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#19">线索化</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#20">线索链表</a>  
&emsp;&emsp;&emsp;<a href="#21">代码</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#22">349.两个数组的交集</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#23">59 滑动窗口的最大值</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#24">94. 二叉树的中序遍历</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#25">258. 各位相加</a>  
<a href="#26">      # recursion terminator</a>  
<a href="#27">      # process logic in current level</a>  
<a href="#28">      # dill down</a>  
<a href="#29">      # reverse the current level status if needed</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#30">242. 有效的字母异位词</a>  
<a href="#31">  # nlog(n)</a>  
<a href="#32">  # o(n) 存储索引</a>  
<a href="#33">  # o(n)map</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#34">104. 二叉树的最大深度</a>  
[toc]
## <a name="0">算法训练营第二周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
### <a name="1">感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
第二周，算法题越来越顺，真正的想把算法题做好，就不要把它当作一个题来做，要把它当作生活中解决问题的工具来考虑，不能任务式编程，就像吃饭睡觉一样，当成一个习惯。
最大的问题：一定不要拖，不能拖。算法题不是值要脑子转得快，练是最重要的切记
```
### <a name="2">第一节课</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
#### <a name="3">哈希表概念</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. 哈希表（Hash table），也叫散列表，是根据关键码值（Key value) 而直接进行访问的数据结构。
2. 他通过吧关键码值映射到表中的一个位置来访问记录，以加快查找的速度。
3. 这个映射函数叫做三裂函数（Hash Function）,存放记录的数组叫做哈希表（或散列表）

#### <a name="4">四件套</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. clarification (搞清题目)
2. possible solution --> optimal(time & space) （找最优化方式）
3. code 
4. test cases

#### <a name="5">二叉树</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="6">概念：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
二叉树是n(n>=0)个结点的有限集合，该集合或者为空集（成为空二叉树），或者由一个 根结点和两棵互不相交。分别称为根结点的左子树右子树的二叉树组成。
##### <a name="7">性质：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. 深度为k的二叉树，最多有 2^k - 1 个结点
2. 二叉树的第i层最多有 2^(i - 1)个结点
3. 在一棵二叉树中，如果叶子结点树为N0,度为2的结点数为N2，则有 N0 = N2 + 1
  [推导过程](https://www.bilibili.com/video/BV1D541167LF/?spm_id_from=333.788.videocard.0)

#### <a name="8">满二叉树</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="9">概念：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
在一个二叉树中，如果所有的分支节点都存在左子树和右子树，并且所有的叶子结点都在同一层上，这个树就是满二叉树。
1. 叶子只能出现在最下一层
2. 只有度为0和度为2的节点

#### <a name="10">完全二叉树</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="11">概念：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
在满二叉树中，从最后一个结点开始，连续去掉任意个结点，即时一棵完全二叉树
##### <a name="12">性质：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. 叶子结点只能出现在最下两层，且最下层的叶子结点都集中在二叉树的左面
2. 完全二叉树中如果有度为1的结点，只可能有一个，且该结点只有左孩子
3. 深度为k的完全二叉树在k-1层上，一定是满二叉树
4. 在同样结点个树的二叉树中，完全二叉树的深度最小
5. 对一个具有n个结点的完全二叉树中从1开始按层序编号，则
   + 结点i的双亲结点为i/2
   + 结点i的左孩子为2 * i
   + 结点i的右孩子为2 * i + 1
   
#### <a name="13">二叉树的存储结构</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. 二叉链表有 n+ 1 个空指针 （2 * n）- (n - 1) 2 * n  是指针个数，n - 1 是边。
2. 三叉链表（增加了指向双亲的指针）

##### <a name="14">二叉树的层序遍历</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. 队列Q初始化
2. 如果二叉树非空，将根指针入队
3. 循环直到队列Q为空
   + q= 队列Q的对头元素出队
   + 访问结点q的数据域
   + 若q结点存在左孩子，则将左孩子的指针入队
   + 若q结点存在有孩子，则将有孩子的指针入队
4. 代码
        ```
        def Bitree(self, root: BitreeNode):
            if root == None:
               retrun
            queue.append(root)
            while queue not None:
                q = queue.popleft()
                visit(q -> data)  
                if q.left:
                   queue.append(q.left)
                if q.right:
                   queue.append.(q.right)
        ```
##### <a name="15">二叉树的前序遍历</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1. 若二叉树的根结点为空，则返回
2. 访问根结点
3. 前序遍历根结点的左子树
4. 前序遍历根结点的右子树
5. 代码 （递归）
   ```
   def preorder(self, root: BiNode):
       if bt == None:
         return
       else:
          visit(bt.val)
          self.preorder(bt.left)
          self.preorder(bt.right)
   ```
  1. （非递归）
    伪代码
 
  ```
    def preorder(self, root:BiNode):
        stack = []
        p = root
        while p is not None || stack is not None:
            whle p:
              visit(p)
              p = stack.append(p)
              p = p.left  
              
            if stack is not None:
              p = stack.pop()
              p = p.right  
           
  ```
  
  
##### <a name="16">二叉树的中序遍历</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
  

 

#### <a name="17">二叉搜索树的特点</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="18">线索</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：
将二叉链表中的空指针域指向前驱结点或后继结点的指针称为线索
##### <a name="19">线索化</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：
使二叉链表中结点的空链域存放前驱或后继信息的过程称为线索化
##### <a name="20">线索链表</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
概念：
加上线索的二叉链表称为线索链表（或线索二叉树）



#### <a name="21">代码</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[349.两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays/)|1|1|
|[59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)|1|1|
|[258. 各位相加](https://leetcode-cn.com/problems/add-digits/)|1|1|
|[412. Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/)|1|1|
|[242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)|1|1|
|[104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)|1|1|
|[94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)|1|1|
|[144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)||0|
|[590. N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)||0|
|[589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)||0|
|[429. N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)||0|


##### <a name="22">349.两个数组的交集</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[349.两个数组的交集](https://leetcode-cn.com/problems/intersection-of-two-arrays/)
```
class Solution:
    from typing import List
     map求解
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        for i in range(len(nums1)):
            dict1[nums1[i]] = i
        for j in range(len(nums2)):
            if nums2[j] in dict1:
                dict2[nums2[j]] = j

        return dict2.keys()

     set求解
    def intersectionSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(nums1) < len(nums2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]

a = Solution()
print(a.intersectionSet([1,4,4,6,7],[3,4,1,3,6]))
```
##### <a name="23">59 滑动窗口的最大值</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)
```
import collections
from typing import List
class Solution:
     双端队列的形式来解决
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        n, res = [], len(nums)
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k,  len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])

        return res

     双端队列的形式来解决
     思考 [i,j]为一个窗口, i - 1为窗口的前一个元素
    def maxSlidingWindowTwo(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        res = []
        n = len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.pop()
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])
        return res

     国际服
     思考：问题的难点在于i - k代表什么，k - 1 代表什么
     i- k 代表 （i - k, i] 是一个窗口  k - 1 是第一个窗口的右边界
    def maxSlidingWindowInternational(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

a = Solution()
print(a.maxSlidingWindowInternational([5,8,3,4,5],2))
```

##### <a name="24">94. 二叉树的中序遍历</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
```
递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    
    def helper(self, root: TreeNode, res: List[int]) -> List[int]:
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)
        else:
            return
 维护一个栈           
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
           while curr:
               stack.append(curr)
               curr = curr.left
           curr = stack.pop()
           res.append(curr.val)
           curr = curr.right   
        return res   
```
##### <a name="25">258. 各位相加</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[258. 各位相加](https://leetcode-cn.com/problems/add-digits/)
```
class Solution:
     循环
    def addDigits(self, num: int) -> int:
        while num > 10:
            num = num // 10 + num % 10
        return num

     递归
    def addDigitsRecursion(self, num: int) -> int:

        # <a name="26">recursion terminator</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        if num < 10:
            return num

        # <a name="27">process logic in current level</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        num = num // 10 + num % 10

        # <a name="28">dill down</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        return self.addDigitsRecursion(num)

        # <a name="29">reverse the current level status if needed</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

     模9
    def addDigitsMold(self, num: int) -> int:
        return (num - 1) % 9 + 1

a = Solution()
print(a.addDigitsMold(456))

```
##### <a name="30">242. 有效的字母异位词</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
```
import collections
class Solution:
    # <a name="31">nlog(n)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
    def isAnagram(self, s: str, t: str) -> bool:
        sl = "".join(sorted(list(s)))
        tl = "".join(sorted(list(t)))
        if sl == tl:
            return True
        else:
            return False

    # <a name="32">o(n) 存储索引</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
    def isAnagramTwo(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
           count[ord(s[i]) - ord('a')] += 1
           count[ord(t[i]) - ord('a')] -= 1
        for i in count:
            if i != 0:
                return False
        return True

    # <a name="33">o(n)map</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
    def isAnagramThree(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in count.values():
            if i != 0:
                return False
        return True



a = Solution()
print(a.isAnagramThree("werty","wtyer"))
```
##### <a name="34">104. 二叉树的最大深度</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
```
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque()
        queue.append(root)
        res = 0
        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            res += 1

        return res
```


