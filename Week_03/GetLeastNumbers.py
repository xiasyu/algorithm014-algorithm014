# 参考链接 https://www.bilibili.com/video/BV1Eb41147dK?from=search&seid=10277900355091596982
from typing import List
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        # 系统堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        res = [-x for x in hp]

        # 自定义堆
        # self.heapSort(arr)
        # res = arr[:k]
        return res


    # 堆排序
    def heapSort(self,arr: List[int]):
        self.buildHeap(arr,len(arr))
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i];
            arr[i] = arr[0]
            arr[0] = temp
            self.buildHeap(arr,i)

    # 生成一个堆
    def buildHeap(self,arr: List[int],n:int):
        lastNode = n - 1
        parent = (lastNode - 1) // 2
        for i in range(parent,-1,-1):
            self.heapify(arr,n,i)

    #一开始写的heapify函数是从顶部开始向下的，所以会出现最大数在最底下冒不上来的情况，但是up写的第二个build_heap函数包含了heapify并且是从底层开始的，所以能生成堆
    def heapify(self, arr: List[int], n: int, i: int):
        # recursion terminator
        if i >= n:
            return

        # procell login in current level
        cr = 2 * i + 2
        tempMax = i
        cl = 2 * i + 1

        if ((cl < n) and (arr[cl] > arr[tempMax])):
            tempMax = cl
        if ((cr < n) and (arr[cr] > arr[tempMax])):
            tempMax = cr
        if tempMax != i:
            temp = arr[tempMax]
            arr[tempMax] = arr[i]
            arr[i] = temp
            # dill down
            self.heapify(arr, n, tempMax)

a = Solution()
print(a.getLeastNumbers([4,10,3,5,1,2],4))