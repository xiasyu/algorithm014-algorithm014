class Solution:
    from  typing import List
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        ans.pop()
        fizzBuzz = {3:"Fizz",5:"Buzz"}
        for i in range(1, n + 1):
            fizzBuzzStr = ""
            for key in fizzBuzz.keys():
                if i % key == 0:
                    fizzBuzzStr += fizzBuzz[key]
            if fizzBuzzStr == "":
                ans.append(str(i))
            else:
                ans.append(fizzBuzzStr)
        return ans
a = Solution()
print(a.fizzBuzz(15))

