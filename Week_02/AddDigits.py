class Solution:
    # 循环
    def addDigits(self, num: int) -> int:
        while num > 10:
            num = num // 10 + num % 10
        return num

    # 递归
    def addDigitsRecursion(self, num: int) -> int:

        # recursion terminator
        if num < 10:
            return num

        # process logic in current level
        num = num // 10 + num % 10

        # dill down
        return self.addDigitsRecursion(num)

        # reverse the current level status if needed

    # 模9
    def addDigitsMold(self, num: int) -> int:
        return (num - 1) % 9 + 1

a = Solution()
print(a.addDigitsMold(456))
