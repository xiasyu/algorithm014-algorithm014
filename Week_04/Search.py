from typing import List
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     if n <= 0:
    #         return -1
    #     left, right = 0, n - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2
    #         if nums[mid] == target:
    #             return mid
    #         if target >= nums[0]:
    #             if nums[mid] < nums[0]:
    #                 nums[mid] = float("inf")
    #         else:
    #             if nums[mid] >= nums[0]:
    #                 nums[mid] = float("-inf")
    #         if target < nums[mid]:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
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


a = Solution()
print(a.search([4,5,6,7,0,1,2],0))