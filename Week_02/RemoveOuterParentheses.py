class Solution:
    # 单调栈
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        stack = []

        # basket is used to store previous value
        basket = ''

        for p in S:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
            basket += p

            if not stack:
                res += basket[1:-1]
                basket = ''
        return res
    # 双指针

    def removeOuterParenthesesTwo(self, S: str) -> str:
        primitive_indices = []
        j, count = 0,0
        for i in range(len(S)):
            if S[i] == '(':
                count += 1
            elif S[i] == ')':
                count -= 1
            if count == 0:
                primitive_indices.append([j, i])
                j = i + 1

        return "".join(S[m+1:n] for m, n in primitive_indices )



a = Solution()
print(a.removeOuterParenthesesTwo("(())"))





