from typing import List
class Solution:
    # 第一种方式 (暴力解法)
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            left = i
            right = i
            height = heights[i]
            # 这一步我在判断heights[left - 1] >= height的时候出错了，>= 我写成了 <,这是不对的。因为只有在大于height的时候left才会想做移动，right同理
            while left - 1 >= 0 and heights[left - 1] >= height:
                left -= 1
            while right + 1 < n and heights[right + 1] >= height:
                right += 1
            max_area = max(max_area, height * (right - left + 1))
        return max_area

    # 第二种方式 （单调栈）
    def largestRectangleArea1(self, heights: List[int]) -> int:
        # 首尾添加0高度的柱子
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for idx_right in range(len(heights)):
            while stack and heights[stack[-1]] > heights[idx_right]:
                h_mid = heights[stack.pop()]
                idx_left = stack[-1]
                res = max(res, h_mid * (idx_right - idx_left - 1))
            stack.append(idx_right)
        return res



a = Solution()
print(a.largestRectangleArea1([1]))