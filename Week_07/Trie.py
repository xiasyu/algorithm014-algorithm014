# class Node:
#     def __init__(self):
#         self.child = [None for _ in range(26)]
#         self.isEnd = False
#
#     def content_key(self, ch):
#         return self.child[ord(ch) - ord('a')]
#
#     def put(self, ch):
#         self.child[ord(ch) - ord('a')] = Node()
#
#     def get(self, ch):
#         return self.child[ord(ch) - ord('a')]
#
#
#
# class Trie:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = Node()
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         p = self.root
#         for ch in word:
#             if not p.content_key(ch):
#                 p.put(ch)
#             p = p.get(ch)
#         p.isEnd = True
#
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         p = self.root
#         for ch in word:
#             if p.content_key(ch):
#                 p = p.get(ch)
#             else:
#                 return False
#         return p.isEnd
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         p = self.root
#         for ch in prefix:
#             if p.content_key(ch):
#                 p = p.get(ch)
#             else:
#                 return False
#         return True
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch,{})
        node[self.end_of_word] = self.end_of_word
        print(self.root)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            else:
                node = node[ch]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            else:
                node = node[ch]
        return True
a = Trie()
a.insert('apple')
# print(a.search('apple'))
# print(a.search('app'))
# print(a.startsWith('app'))
a.insert('app')
print(a.search('app'))
print(a.search('apple'))

