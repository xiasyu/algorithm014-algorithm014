from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in range(len(bills)):
            money = bills[i]
            if money == 5:

                five += 1
            elif money == 10:
                if five <= 0:
                    # print(i)
                    return False
                five -= 1
                ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
a = Solution()
print(a.lemonadeChange([5,5,10,10,20]))