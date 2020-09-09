class ListNode:
    def __init__(self, s:str, left:int, right:int):
        self.s = s
        self.left = left
        self.right = right

import collections
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # self.dfs(0,0,n,"",res)
        self.bfs(n,res)
        return res

    def dfs(self, left:int, right:int, n:int, s:str, res:List[str]):

        # recusion termimal
        if left == n and right == n:
            res.append(s)

        # process current logic

        # dill down
        if left < n:
            self.dfs(left + 1, right, n, s + "(", res)

        if right < left and right < n:
            self.dfs(left, right + 1, n, s + ")", res)

        # restore

    def bfs(self, n:int, res:List[str]) -> List[str]:
        root = ListNode("",n,n)
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:

            node = queue.popleft()
            if node.left == 0 and node.right == 0:
                res.append(node.s)

            if node.left > 0:
                listNode = ListNode(node.s + "(",node.left - 1,node.right)
                queue.append(listNode)

            if node.right > node.left and node.right > 0:
                listNode = ListNode(node.s + ")",node.left,node.right - 1)
                queue.append(listNode)

a = Solution()
print(a.generateParenthesis(3))

