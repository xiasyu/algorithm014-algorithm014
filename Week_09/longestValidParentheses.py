from typing import List
class Solution:
    # 暴力解法
    def longestValidParentheses(self, s: str) -> int:
        # 首先定义一个 isValid的函数，判断字串是否是合法字串
        # 然后截取测试长度的字串，进行判断。如果截取的字串为有效字串，则长度为合法字串（由长到短开始截取）

        # 定义的判断字串是否合法的函数
        def isValid(subs):
            stack = []
            n = len(subs)
            for i in range(n):
                if subs[i] == '(':
                    stack.append('(')
                elif stack != [] and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []

        # 开始进行遍历
        n = len(s)
        if n < 2:
            return 0
        #因为有效字串一定是偶数，如果总长度为偶数，则边界n否则为n-1。每次遍历都减去两个长度。
        for i in range(n if n % 2 == 0 else n - 1, 0 , -2):
            for j in range(n - i + 1):
                if isValid(s[j:j+i]):
                    return i
        return 0

    #第二种动态规划的方法
    def longestValidParentheses1(self, s: str) -> int:
        # 首先找到状态转移方程
        # dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i-1] - 2]
        return max(dp)

    # 第三种方法 栈
    def longestValidParentheses3(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        stack = [-1]
        max_length = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(length, max_length)
        return max_length

    # 第四种方法 正向逆向结合法
    def longestValidParentheses4(self, s: str) -> int:
        def lengthIndifferent(s, fromLeft) -> int:
            max_length = 0
            left_num = 0
            right_num = 0
            if fromLeft == True:
                for c in s:
                    if c == '(':
                        left_num += 1
                    else:
                        right_num += 1
                    if left_num == right_num:
                        max_length = max(max_length, 2 * left_num)

                    elif right_num > left_num:
                        right_num = left_num = 0
            if fromLeft == False:
                for c in s[::-1]:
                    if c == '(':
                        left_num += 1
                    else:
                        right_num += 1
                    if left_num == right_num:
                        max_length = max(max_length,2 * left_num)
                    elif right_num < left_num:
                        right_num = left_num = 0
            return max_length


        max_from_left = lengthIndifferent(s,True)
        max_from_right = lengthIndifferent(s,False)

        return max(max_from_left,max_from_right)

a = Solution()
print(a.longestValidParentheses4("(()"))


