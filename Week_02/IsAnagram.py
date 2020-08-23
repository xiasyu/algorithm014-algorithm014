import collections
class Solution:
    # nlog(n)
    def isAnagram(self, s: str, t: str) -> bool:
        sl = "".join(sorted(list(s)))
        tl = "".join(sorted(list(t)))
        if sl == tl:
            return True
        else:
            return False

    # o(n) 存储索引
    def isAnagramTwo(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
           count[ord(s[i]) - ord('a')] += 1
           count[ord(t[i]) - ord('a')] -= 1
        for i in count:
            if i != 0:
                return False
        return True

    # o(n)map
    def isAnagramThree(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in count.values():
            if i != 0:
                return False
        return True





a = Solution()
print(a.isAnagramThree("werty","wtyer"))