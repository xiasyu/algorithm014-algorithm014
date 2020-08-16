class Solution:
    from typing import List
        # 暴力求解1 (暂时不对)
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     i = 0
    #     j = len(heights) - 1
    #     maxArea  = 0
    #     while i <= j:
    #         tempMax = 0
    #         different = j - i + 1
    #         tempMax = different * min(heights[i:j + 1])
    #         if heights[i] <= heights[j]:
    #             i += 1
    #         else:
    #             j -= 1
    #         print(tempMax)
    #         if maxArea < tempMax:
    #             maxArea = tempMax
    #     return  maxArea

    # # 暴力求解 2
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
    #     n = len(heights)
    #     for i in range(len(heights)):
    #         height = heights[i]
    #         left = i
    #         right = i
    #         while (left - 1 >= 0) and (heights[left - 1] >= height):
    #             left -= 1
    #         while (right + 1 < n) and (heights[right + 1] >= height):
    #             right += 1
    #         ans = max(ans,height * (right - left + 1))
    #     return ans







    # 单调栈 + 常数优化
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
        # print(left, right, mono_stack)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0

        return ans

a = Solution()
print(a.largestRectangleArea([6,7,5,2,4,5,9,3]))
