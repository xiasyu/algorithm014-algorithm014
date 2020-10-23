from typing import List
class Solution:
    # 单调栈 解法（嵌套了 84 求最大矩形面积 的完整代码）
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        max_area = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    # 计算矩形的最大面积
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        max_area = 0
        stack = []
        for idx_right in range(len(heights)):
            while stack and heights[stack[-1]] > heights[idx_right]:
                h_mid = heights[stack.pop()]
                idx_left = stack[-1]
                max_area = max(max_area, h_mid * (idx_right - idx_left - 1))
            stack.append(idx_right)
        return max_area

    # 动态规划 优化 暴力解法
    def maximalRectangle1(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                row_with = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                for k in range(i, -1, -1):
                    row_with = min(row_with,dp[k][j])
                    max_area = max(max_area,row_with * (i - k + 1))
        return max_area


a = Solution()
print(a.maximalRectangle1([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))







