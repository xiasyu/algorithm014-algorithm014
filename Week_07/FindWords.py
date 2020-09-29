import collections
from typing import List
dx = [-1,1,0,0]
dy = [0,0,-1,1]
END_OF_WORD = '#'
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words: return []
        self.result = set()

        # 构建trie
        root = collections.defaultdict()
        for word in words:
            node = root # 这一步是为了使每个单词的开头字符都在root层，也就是最顶层
            for ch in word:
                node = node.setdefault(ch,collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        # 开始查找
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    # dfs
                    self.dfs(board,i,j,'',root)
        return list(self.result)

    # dfs(深度优先遍历)
    def dfs(self,borad,i,j,cur_word,cur_dict):
        cur_word += borad[i][j]
        cur_dict = cur_dict[borad[i][j]]
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        temp, borad[i][j] = borad[i][j], '@'
        for k in range(4):
            x,y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and borad[x][y] != '@' and borad[x][y] in cur_dict:
                self.dfs(borad,x,y,cur_word,cur_dict)
        borad[i][j] = temp



a = Solution()
print(a.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath","pea","eat","rain"]))

