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
   
   ![-w962](media/15969752147669/15972380508566.jpg)

   
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
##### [70.爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
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
```
```   
##### [66.加一](https://leetcode-cn.com/problems/plus-one/)
```

class Solution:
    
    def __init__(self):
          pass
    from typing import List

    # 方法一
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
        
    #方法二
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

     # 方法三
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

##### [283.移动零](https://leetcode-cn.com/problems/move-zeroes/)
```
class Solusion:
    def __init__(self):
        pass
    # 第一种方法
    from typing import List
    # def moveZeroes(self, nums: List[int]) -> None:
    #     i = 0
    #     for j in range(0, len(nums)):
    #         if nums[j] != 0:
    #             nums[i] = nums[j]
    #             i += 1
    #     for a in range( i, len(nums)):
    #         nums[a] = 0       
    #     print(nums)    


     # 第二种方法 (增加了一个新数组，不用也行)
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
##### [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)
```
class Solution:
    from typing import List
    # 第一种解法
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            # 不等的时候将i的值存储到 ++j上
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i] 
        return j + 1

a = Solution()
print(a.removeDuplicates([1,1,2,3,4,4,5]))
```

##### [1.两数之和](https://leetcode-cn.com/problems/two-sum/)
```
class Solution:
    def __init__(self):
        pass

    from typing import List
    # 第一种方式 o(n^2)
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

     
     # 第二种方式 遍历法
    def twoSumTwo(self, nums: List[int], target: int) -> List[int]:          
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0,0]
    
    # 第三种方式 hash方式实现
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        tempdict = {}
        for i in range(0, len(nums)):
            tempdict[nums[i]] = i
        for i in range(0, len(nums)):
            value = target - nums[i]
            if (value in tempdict) & (i != tempdict[value]):
                return [i, tempdict[value]]
        return [0,0]  

    # 第四种方式 哈希方式 不是很好理解 （这个方式的理解，可以理解为 原始序列和差的map是逆序的，相当，一定存在一前一后的问题。一个的出现必定在另一个的后面）
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

##### [11.盛水最多容器](https://leetcode-cn.com/problems/container-with-most-water/)
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

##### [189.旋转数组 (第三种方式没有看懂)](https://leetcode-cn.com/problems/rotate-array/)
```
class Solution:
    from typing import List
    # 这个方法耗时
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

    # 第三种解法： 使用环状替换
    # 思路：因为
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
# print(a.rotate([1,2,3,4,5],4))
# print(a.rotateTwo([1,2,3,4,5],2),'\n')
print(a.rotateThree([1,2,3,4,5,6],2))
```

##### [24.两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
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

##### [15.三数之和](https://leetcode-cn.com/problems/3sum/)
```
class Solution:
    def __init__(self):
        pass

    from typing import List
    #第一种做法：暴力
    def threeSums(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [i, j, k]


    # 第二种做法：双指针法
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


   
