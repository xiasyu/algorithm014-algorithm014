<a name="index">**Index**</a>
<a href="#0">算法训练营</a>  
&emsp;<a href="#1">第一周</a>  
&emsp;&emsp;<a href="#2">感想</a>  
&emsp;&emsp;&emsp;<a href="#3">算法训练营一周感想</a>  
&emsp;&emsp;<a href="#4">第一节课</a>  
&emsp;&emsp;&emsp;<a href="#5">学习算法的方式</a>  
&emsp;&emsp;&emsp;<a href="#6">软件</a>  
&emsp;&emsp;&emsp;<a href="#7">知识点 </a>  
&emsp;&emsp;&emsp;<a href="#8">时间复杂度</a>  
&emsp;&emsp;&emsp;<a href="#9">主定理：</a>  
&emsp;&emsp;&emsp;<a href="#10">涉及到的算法题</a>  
&emsp;&emsp;&emsp;<a href="#11">代码 </a>  
&emsp;&emsp;&emsp;&emsp;<a href="#12">[70.爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#13">LRUCatch</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#14">[66.加一](https://leetcode-cn.com/problems/plus-one/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#15">[283.移动零](https://leetcode-cn.com/problems/move-zeroes/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#16">[26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#17">[1.两数之和](https://leetcode-cn.com/problems/two-sum/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#18">[11.盛水最多容器](https://leetcode-cn.com/problems/container-with-most-water/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#19">[189.旋转数组 (第三种方式没有看懂)](https://leetcode-cn.com/problems/rotate-array/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#20">[24.两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#21">[15.三数之和](https://leetcode-cn.com/problems/3sum/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#22">[21.合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)</a>    
&emsp;&emsp;&emsp;&emsp;<a href="#24">[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#25">[20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#26">[155. 最小栈](https://leetcode-cn.com/problems/min-stack/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#27">[84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#28">[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#29">[641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)</a>  
&emsp;&emsp;&emsp;<a href="#30">栈和队列</a>  

# <a name="0">算法训练营</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="1">第一周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
### <a name="2">感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
#### <a name="3">算法训练营一周感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
    我进入算法训练营学习算法的目标比较明确，就是想学习一种不同于普通程序员的东西，在我接触算法以前，我的脑子里就有两种程序员：懂算法的程序员和不懂算法的程序员。有点类似于小怪和boss😄
    算上体验课，在算法训练营待了两周了，到现在给我的感觉就是：累，难，过后倍儿有成就感。
    昨天之前还好，当我遭遇到“柱状图中最大的矩形”这道题目的时候，暴力解法我瞬间理解，总以为自己聪明，当我试着去理解“单调栈+常数优化”的算法时，我瞬间懵逼，仿佛我站在一维空间仰视二维空间里的不知名生物一样，这都是些啥，一步一步栈进栈出，一步一步数据的复杂调用，目不转睛的看了两个小时我终于弄清楚了这个算法栈结构的调用过程，当我尝试阅读代码的时候，我再次陷入了懵逼状态，我的天，这是啥，我脑海中理解的复杂结构的代码，你竟然三言两语就给我搞完了，俗话说浓缩的都是精华，但是精华里包含的东西，我实在是看不透啊。于是我一遍一遍在脑海里浮现数组的栈入栈出过程，一遍又一遍，直到又过了两个小时......还是没搞懂。不甘心的我趴在了床上，脑子好像慢慢的变得清醒。脑子里立马将代码和图的移动过程结合了起来，right数组存储右边界，left数组存储左边界，mono_stack是栈入栈出的过程，我的脑海里将数据结构和图的移动联系起来，大脑又开始高速运转，通了😄
    我终于明白了，不是因为我突然变得聪明了，是因为我对数据记忆已经非常深刻，对图的移动逻辑也理解的比较透彻，所以在我高强度牺牲脑细胞的前提下，思路慢慢的融会贯通了。于是我总结了这几个克服困难算法的过程
    1、10分钟看不懂立马看题解
    2、题解看不懂，说明这个问题你没有接触过，死背数据，死记图或者数据的移动流程，在大脑里一遍遍的过数据交换的思路
    3、懂不是一个结果，是一个过程，等你真正的记住了数据交换流程，思路自己就清晰起来，一点就通的情况会有，那是在你的知识储备非常丰富的时候，或者说你的算法底子非常好的时候。如果不是，你就把这道题的数据交换过程背到滚瓜烂熟。用一个特例来走过程。
    4、五毒神掌，不会做的题，看完题解，明白了之后，总会忘。脑子这个东西，真的是有保质期的。
    5.用到生活中的事例中去，去强化你对算法的理解，一定要在你没忘记这道题的思路之前，深刻的强化他。
    6.最重要的一点：一定不能拖，不能拖。浪费的时间早晚都要补回来，补不回来就真的失去了💔
### <a name="4">第一节课</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
#### <a name="5">学习算法的方式</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.不用看书（算法导论也不用看，书和资料在于精不在于多）
   注：看拉布拉多算法总结
2.科学做题：累了消遣娱乐活动 （将抖音时间和娱乐时间换成刷题，但是正经做题的时候不行啊）-> 刷简单（捏软柿子）
   注：消遣和娱乐都做算法
   
   ![-w962](media/15969752147669/15972380508566.jpg)

   
#### <a name="6">软件</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.scapple
2.mindnode
3.百度脑图
#### <a name="7">知识点 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
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
  
#### <a name="8">时间复杂度</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
big o notation
o(1) : Constant complexity 常数复杂度
o(log n) : Logarithmic Complexity 对数复杂度
o(n) : Linear Complexity 线行时间复杂度
o(n^2) : N square Complexity 平方
o(n^3) : N cubic Complexity 立方
o(2^n) : Exponential Growth 指数
o(n!) : Factorial 阶乘
![-w1289](media/15934870103065/15961775767111.jpg)


#### <a name="9">主定理：</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
n指的是搜索空间里的节点总数
二叉树的前序、中序、后序的时间复杂度是o(n)
图的遍历的时间复杂度：o(n)
搜索算法:DFS、BFS时间复杂度是多少？o(n)
二分查找的时间复杂度是多少？o(logn) 
  
  
####递归的两个要素：
1、递归边界条件，确定递归到何时终止，也叫递归出口
2、递归模式：大问题如何分解为小问题的，也叫递归体


#### <a name="10">涉及到的算法题</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.删除排序数组中的重复项
2.盛最多水的容器
3.N叉树的前序遍历
4.二叉树的前序遍历
5.[递归代码模版](https://shimo.im/docs/EICAr9lRPUIPHxsH/read)
6.二叉树的最大深度
7.验证二叉搜索树
8.leetcode 146 LRU缓存机制
#### <a name="11">代码 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[70.爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)|1|1|
|[66.加一](https://leetcode-cn.com/problems/plus-one/)|简单|4|
|[283.移动零](https://leetcode-cn.com/problems/move-zeroes/)|简单|4|
|[26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)|简单|4|
|[1.两数之和](https://leetcode-cn.com/problems/two-sum/)|简单|4|
|[11.盛水最多容器](https://leetcode-cn.com/problems/container-with-most-water/)|简单|4|
|[189.旋转数组 (第三种方式没有看懂)](https://leetcode-cn.com/problems/rotate-array/)|简单|3|
|[15.三数之和](https://leetcode-cn.com/problems/3sum/)|中等|2|
|[21.合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)|简单|2|
|[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)|简单|3|
|[84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)|困难|1|


##### <a name="12">[70.爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1.爬楼梯
class Solution:
     方法一  递归
    def climbStairs(n: int) -> int:
       dp = {}
       dp[1] = 1
       dp[2] = 2
       for i in range(3, n + 1):
           dp[i] = dp[i - 1] + dp[i - 2]
       return dp[n]

         方法二 动态规划
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

    方法三 递归缓存
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
##### <a name="13">LRUCatch</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
```   
##### <a name="14">[66.加一](https://leetcode-cn.com/problems/plus-one/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```

class Solution:
    
    def __init__(self):
          pass
    from typing import List

     方法一
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1
        for i in range(0, digits.__len__())[::-1]:
            value = 0
            value = digits[i] + temp
            digits[i] =  value % 10
            temp = value // 10
        if temp == 1:
            import numpy as np
            tempDigits = np.zeros((digits.__len__() + 1), dtype=np.int)
            tempDigits [0] = 1
            return tempDigits
        return digits
        
    方法二
    def plusOneTwo(self, digits: List[int]) -> List[int]:
        for i in range(0, digits.__len__())[::-1]:
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        temoDigits = [0] * (digits.__len__() + 1) 
        temoDigits[0] = 1
        return temoDigits   

      方法三
    def plusOneThree(self, digits: List[int]) -> List[int]:
        for i in range(0, digits.__len__())[::-1]:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        tempDigids = [0] * (digits.__len__() + 1)
        tempDigids[0] = 1
        return tempDigids
                

a = Solution()
print(a.plusOne([1,2,3])) 
print(a.plusOneTwo([9,9,9]))
print(a.plusOneThree([9,9,9]))
```

##### <a name="15">[283.移动零](https://leetcode-cn.com/problems/move-zeroes/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solusion:
    def __init__(self):
        pass
     第一种方法
    from typing import List
     def moveZeroes(self, nums: List[int]) -> None:
         i = 0
         for j in range(0, len(nums)):
             if nums[j] != 0:
                 nums[i] = nums[j]
                 i += 1
         for a in range( i, len(nums)):
             nums[a] = 0       
         print(nums)    


      第二种方法 (增加了一个新数组，不用也行)
    def moveZerosTwo(self, nums: List[int]) -> None:
        tempNums = []
        for i in range(0, len(nums)):
            if nums[i] != 0:
                tempNums.append(nums[i])
        for i in range(len(tempNums), len(nums)):
            tempNums.append(0)
        print(tempNums)


a = Solusion()
a.moveZeroes([1,0,0,4,0,5,0,3])
a.moveZerosTwo([1,0,0,4,0,5,0,3])
```
##### <a name="16">[26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    from typing import List
     第一种解法
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
             不等的时候将i的值存储到 ++j上
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i] 
        return j + 1

a = Solution()
print(a.removeDuplicates([1,1,2,3,4,4,5]))
```

##### <a name="17">[1.两数之和](https://leetcode-cn.com/problems/two-sum/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    def __init__(self):
        pass

    from typing import List
     第一种方式 o(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        different = []
        for i in range(0, len(nums)):
            value = target - nums[i]
            different.append(value)
        for i in range(0, len(nums)):
            for j in range(0, len(different)):
                if (nums[i] == different[j]) & (i != j):
                    return [i,j]
        return [0,0]     

     
      第二种方式 遍历法
    def twoSumTwo(self, nums: List[int], target: int) -> List[int]:          
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0,0]
    
    第三种方式 hash方式实现
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        tempdict = {}
        for i in range(0, len(nums)):
            tempdict[nums[i]] = i
        for i in range(0, len(nums)):
            value = target - nums[i]
            if (value in tempdict) & (i != tempdict[value]):
                return [i, tempdict[value]]
        return [0,0]  

     第四种方式 哈希方式 不是很好理解 （这个方式的理解，可以理解为 原始序列和差的map是逆序的，相当，一定存在一前一后的问题。一个的出现必定在另一个的后面）
    def twoSumHashTwo(self, nums: List[int], target: int) -> List[int]:
        tempHash = {}
        for i in range(0, len(nums)):
            value = target - nums[i]
            print(value,tempHash)
            if value in tempHash:
                return [tempHash[value],i]
            tempHash[nums[i]] = i   
             

a = Solution()
print(a.twoSumHash([3,4,11,5],8))
```

##### <a name="18">[11.盛水最多容器](https://leetcode-cn.com/problems/container-with-most-water/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    from typing import List
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = height.__len__() - 1
        res = 0
        while i < j:
            area = min(height[i], height[j])*(j-i)
            if area > res:
               res = area
            if height[i] < height[j]:
                i +=1
            else:
                j -= 1
        return res

a = Solution()
print(a.maxArea([1,3,5,2,9]))
```

##### <a name="19">[189.旋转数组 (第三种方式没有看懂)](https://leetcode-cn.com/problems/rotate-array/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    from typing import List
     这个方法耗时
    def rotate(self, nums: List[int], k: int) -> List[int]:
        k = k % len(nums)
        if k >= len(nums):
            return nums
        for i in range(0,k):
            nums.insert(0,nums[len(nums) - 1 - i])   

        for i in range(0, k):
            nums.pop()  
        return nums      
        

    def rotateTwo(self, nums: List[int], k: int) -> List[int]:
        temp = 0 
        previpus = 0
        k = k % len(nums)
        if k >= len(nums):
            k = k - len(nums)
        for i in range(0,k):
            previpus = nums[-1]
            for j in range(0, len(nums)):
                temp = nums[j]
                nums[j] = previpus
                previpus = temp
        return nums

     第三种解法： 使用环状替换
     思路：因为
    def rotateThree(self, nums: List[int], k: int) -> List[int]:
        k = k % len(nums)
        count = 0
        for start in range(0, len(nums)):
            if count >= len(nums):
                return nums
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break
        return nums


a = Solution()
 print(a.rotate([1,2,3,4,5],4))
 print(a.rotateTwo([1,2,3,4,5],2),'\n')
print(a.rotateThree([1,2,3,4,5,6],2))
```

##### <a name="20">[24.两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
    
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = head
            head = first_node.next

        return dummy.next
```

##### <a name="21">[15.三数之和](https://leetcode-cn.com/problems/3sum/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    def __init__(self):
        pass

    from typing import List
    第一种做法：暴力
    def threeSums(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [i, j, k]


     第二种做法：双指针法
    def threeSumSort(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for first in range(0, len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            third = len(nums) - 1
            target = -nums[first]
            for second in range(first + 1, len(nums)):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -=  1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans            




a = Solution()
print(a.threeSums([1,2,3,-4]))
print(a.threeSumSort([1,2,3,-4]))
```
##### <a name="22">[21.合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
 定义一个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

 定义一个单链表
class LinkList:
    def __init__(self):
        self.head = None

    def initList(self,data) -> ListNode:
        #创建头节点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # <a name="23">逐个为data内的数据创建节点，建立链表</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return  r

     输出一个链表
    def printList(self, head: ListNode):
        if head == None:
            return
        node = head
        while node:
            print(node.val)
            node = node.next

     1、 合并两个有序链表 (使用迭代)
    def mergeTwoListsIteration(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev_node = dummy
        while (l1 is not None) & (l2 is not None):
            if l1.val < l2.val:
                prev_node.next = l1
                l1 = l1.next
            else:
                prev_node.next = l2
                l2 = l2.next
            prev_node = prev_node.next
        if l1 is not None:
            prev_node.next = l1
        else:
            prev_node.next = l2

        return dummy.next


     2、使用递归
    def mergeTwoListsRecursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursion(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursion(l1,l2.next)
            return l2
 初始化链表
l1 = LinkList()
 创建一个链表
l1.initList([1,3,5,7,9])

 输出一个链表
 l1.printList(l1.head)


 初始化第二个链表
l2 = LinkList()
 创建第二个链表
l2.initList([2,4,6,8,10])

 输出第二个个链表
 l2.printList(l2.head)

 迭代合并链表
mergeLinkList = LinkList()
 printMergeLinkList1 = mergeLinkList.mergeTwoListsIteration(l1.head,l2.head)
 mergeLinkList.printList(printMergeLinkList1)

 递归合并链表
printMergeLinkList2 = mergeLinkList.mergeTwoListsRecursion(l1.head,l2.head)
mergeLinkList.printList(printMergeLinkList2)
```

##### <a name="24">[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Solution:
    def __init__(self):
        pass

    from  typing import List
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:

            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

        print(nums1)

a = Solution()
a.merge([2,3,7,8,0,0,0],4,[1,3,6],3)
```

##### <a name="25">[20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>

##### <a name="26">[155. 最小栈](https://leetcode-cn.com/problems/min-stack/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="27">[84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
  暴力求解 1
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        for i in range(len(heights)):
            height = heights[i]
            left = i
            right = i
            while (left - 1 >= 0) and (heights[left - 1] >= height):
                left -= 1
            while (right + 1 < n) and (heights[right + 1] >= height):
                right += 1
            ans = max(ans,height * (right - left + 1))
        return ans
   单调栈 + 常数优化
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1

            mono_stack.append(i)
         print(left, right, mono_stack)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0

        return ans      
        
```
##### <a name="28">[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
##### <a name="29">[641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your deata sturcture here. Set the size of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]


    def insertFront(self, value: int) -> bool:
        """
        Add an item at the front to Deque. Return true if the operation is  successful.
        """

        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True


    def insertLast(self, value: int) -> bool:
        """
         
        Adds an item at the rear of Deque. Return true if the operation is successful. 
        """
        if self.isFull():
          return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity

        return True

    def deleteFront(self) -> bool:

        """
          
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
          return False
        self.front = (self.front + 1) % self.capacity
        return True



    def deleteLast(self) -> bool:
        """
       
        Deletes an item from the front to Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self) -> int:
        """
        
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
         """
         
         Get the last item from the deque.
         """
         if self.isEmpty():
             return -1
         return self.arr[(self.rear - 1 + self.capacity) % self.capacity]


    def isEmpty(self) -> bool:
        """
         
        hecks whether the circular deque is empty or not.
        """
        return self.front == self.rear



    def isFull(self) -> bool:
        """
        
        Checks whether the circular deque is full or not
        """
        return (self.rear + 1) % self.capacity == self.front
 ```
#### <a name="30">栈和队列</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.Stack、Queue、Deque的原理和操作复杂度
2.PriorityQueue的特点和操作复杂度
3.查询Stack、Queuq、Deque、PriorityQueue的系统接口方法
4.作业：用新的代码写一遍这个代码
![-w1238](media/15969752147669/15973765968957.jpg)
5.priority queue
6.python soruce code stack 搜索方式
7.vector
8.时间复杂度
![-w1215](media/15969752147669/15973778332743.jpg)
9.[python 的 heapq](https://docs.python.org/2/library/heapq.html)
10.[高性能的container库](https://docs.python.org/2/library/collections.html)
11.最近相关性的都可以用栈来解决，先来后到也是一样
12.[20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
13.

   
