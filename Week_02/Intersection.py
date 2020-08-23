class Solution:
    from typing import List
    # map求解
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        for i in range(len(nums1)):
            dict1[nums1[i]] = i
        for j in range(len(nums2)):
            if nums2[j] in dict1:
                dict2[nums2[j]] = j

        return dict2.keys()

    # set求解
    def intersectionSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(nums1) < len(nums2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]


    # set 求解 2


a = Solution()
print(a.intersectionSet([1,4,4,6,7],[3,4,1,3,6]))