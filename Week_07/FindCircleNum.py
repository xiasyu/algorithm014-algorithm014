from typing import List
class Solution:


    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        if not M[0]: return 0
        n = len(M)
        parents = list(range(n))

        def find(parents, x):
            while x != parents[x]:
                temp = parents[x]
                # 将父结点父给自己
                parents[x] = parents[temp]
                x = temp
            return x

        def union(parents, x, y):
            x_root = find(parents, x)
            y_root = find(parents, y)
            if x_root != y_root:
                parents[x_root] = y_root

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    union(parents, i, j)
        res = set()
        for i in range(n):
            res.add(find(parents, i))
        return len(res)


a = Solution()
print(a.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))