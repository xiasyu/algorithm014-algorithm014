class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.replace(' ','20%')
        # s = '20%'.join(s.split(' '))
        replaceS = ''
        for idx, val in enumerate(s):
            if val == ' ':
                replaceS += '%20'
            else:
                replaceS += val
        return replaceS
a = Solution()
print(a.replaceSpace("We are happy."))