#88. 合并两个有序数组 https://leetcode-cn.com/problems/merge-sorted-array/
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
