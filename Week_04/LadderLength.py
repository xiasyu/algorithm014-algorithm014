from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) == 0 or endWord not in wordList:
            return 0
        wordListSet = set(wordList)
        if beginWord in wordListSet:
            wordListSet.remove(beginWord)
        word_len = len(beginWord)
        q = deque()
        q.append(beginWord)
        visit = set(beginWord)
        step = 1

        while q:
            queuesize = len(q)
            for i in range(queuesize):
                visitWord = q.popleft()
                visitWordList = list(visitWord)
                for j in range(word_len):
                    origin_c = visitWordList[j]
                    for k in range(26):
                        visitWordList[j] = chr(ord('a')+ k)
                        next_w = ''.join(visitWordList)
                        if next_w in wordListSet:
                            if next_w == endWord:
                                return step + 1
                            if next_w not in visit:
                                q.append(next_w)
                                visit.add(next_w)
                    visitWordList[j] = origin_c
            step += 1
        return 0


a = Solution()
print(a.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))