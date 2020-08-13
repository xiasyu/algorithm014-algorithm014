class Solusion:
    def __init__(self):
        pass
    # 第一种方法
    from typing import List
    # def moveZeroes(self, nums: List[int]) -> None:
    #     i = 0
    #     for j in range(0, len(nums)):
    #         if nums[j] != 0:
    #             nums[i] = nums[j]
    #             i += 1
    #     for a in range( i, len(nums)):
    #         nums[a] = 0       
    #     print(nums)    


     # 第二种方法 (增加了一个新数组，不用也行)
    def moveZerosTwo(self, nums: List[int]) -> None:
        tempNums = []
        for i in range(0, len(nums)):
            if nums[i] != 0:
                tempNums.append(nums[i])
        for i in range(len(tempNums), len(nums)):
            tempNums.append(0)
        print(tempNums)


a = Solusion()
a.moveZeroes([1,0,0,4,0,5,0,3])
a.moveZerosTwo([1,0,0,4,0,5,0,3])
