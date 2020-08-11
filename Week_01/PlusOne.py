
class Solution:
    
    def __init__(self):
          pass
    from typing import List

    # 方法一
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1
        for i in range(0, digits.__len__())[::-1]:
            value = 0
            value = digits[i] + temp
            digits[i] =  value % 10
            temp = value // 10
        if temp == 1:
            import numpy as np
            tempDigits = np.zeros((digits.__len__() + 1), dtype=np.int)
            tempDigits [0] = 1
            return tempDigits
        return digits
        
    #方法二
    def plusOneTwo(self, digits: List[int]) -> List[int]:
        for i in range(0, digits.__len__())[::-1]:
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        temoDigits = [0] * (digits.__len__() + 1) 
        temoDigits[0] = 1
        return temoDigits   

     # 方法三
    def plusOneThree(self, digits: List[int]) -> List[int]:
        for i in range(0, digits.__len__())[::-1]:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        tempDigids = [0] * (digits.__len__() + 1)
        tempDigids[0] = 1
        return tempDigids
                

a = Solution()
print(a.plusOne([1,2,3])) 
print(a.plusOneTwo([9,9,9]))
print(a.plusOneThree([9,9,9]))

    