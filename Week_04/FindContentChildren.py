from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        gn = len(g)
        sn = len(s)
        n = min(gn, sn)
        num = 0
        gindex = 0
        sindex = 0
        while gindex < gn and sindex < sn:
            if g[gindex] > s[sindex]:
                sindex += 1
            elif g[gindex] <= s[sindex]:
                gindex += 1
                sindex += 1
                num += 1

        return num

a = Solution()
print(a.findContentChildren([1,2,3], [1,1]))

