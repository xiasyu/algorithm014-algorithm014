<a name="index">**Index**</a>
&emsp;<a href="#0">第七周</a>  
&emsp;<a href="#1">字典树</a>  
&emsp;&emsp;<a href="#2">字典树的特点</a>  
&emsp;&emsp;<a href="#3">trie树的核心思想</a>  
&emsp;<a href="#4">并查集</a>  
&emsp;&emsp;<a href="#5">适应场景</a>  
&emsp;&emsp;<a href="#6">基本操作</a>  
&emsp;&emsp;&emsp;<a href="#7">代码 </a>  
&emsp;&emsp;&emsp;&emsp;<a href="#8">Trie代码模版1</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#9">Trie代码模版2</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#10">208. 实现 Trie (前缀树)</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#11">208. 实现 Trie (前缀树)感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#12">212. 单词搜索 II</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#13">212. 单词搜索 II感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#14">547. 朋友圈</a>  
&emsp;&emsp;&emsp;&emsp;&emsp;<a href="#15">547. 朋友圈感想</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#16">括号的生成</a>  
&emsp;&emsp;&emsp;&emsp;<a href="#17">八皇后</a>  
[toc]
## <a name="0">第七周</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
## <a name="1">字典树</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
字典树：即trie树，也叫单词查查找树或键树，是一种树形结构。典型应用是用于统计和排序大量的字符串，（但不仅限于字符串）所以经常被搜索引擎系统用于文本词频统计
他的优点是：最大限度的减少无谓的字符串比较，查询效率比哈希表高
### <a name="2">字典树的特点</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.结点本身不存完整单词
2.从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串
3.每个节点的所有子结点路径代表的字符都不相同
### <a name="3">trie树的核心思想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.trie树的核心思想是空间换时间
2.利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
## <a name="4">并查集</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
### <a name="5">适应场景</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.组团，配对问题
### <a name="6">基本操作</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
1.makeSet(s):新建一个新的并查集，其中包含s个单元素集合
2.unionSet(x,y):把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并
3.find(x):找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了


#### <a name="7">代码 </a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
|题目|困难程度|完成次数|
|--:|--:|--:|
|[208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)|1|1|
|[212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)|1|1|
|[547. 朋友圈](https://leetcode-cn.com/problems/friend-circles/)|1|1|


##### <a name="8">Trie代码模版1</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
// 创建结点
class Node:
     def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False
     def content_key(self):
         return self.child[ord(ch) - ord('a')]
     def put(self,ch):
         self.child[ord(ch) - ord('a')] = Node()
     def get(self,ch):
         return self.child[ord(ch) - ord('a')]
//创建对象       
class Trie
      def __init__(self):
          self.root = Node()
      // 插入
      def insert(self, word:str):
           p = self.root
           for ch in word:
               if not p.content_key(ch):
                  p.put(ch)
               p = p.get(ch)
           p.isEnd = True
           
      // 查询（完全匹配）
      def search(self, word:str) -> bool:       
        p = self.root
        for ch in word:
            if p.content_key(ch):
               p = p.get(ch)
            else:
               return False
        return p.isEnd
        
        // 查询（前缀）          
        def startWith(self, prefix:str) -> bool:
            p = self.root
            for ch in prefix:
                if p.content_key(ch):
                   p = p.get(ch)
                else:
                   return False
             return True         
               
                    
```
##### <a name="9">Trie代码模版2</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
class Trie:
      def __init__(self):
          self.root = {}
          self.end_of_word = '#'
      // 插入
      def insert(self, wrod:str):
          node = self.root
          for ch in word:
               node = node.setdefault(char, {}) 
          node[self.end_of_word] = self.end_of_word
          
      // 搜索
      def search(self, word:str):
          node = self.root
          for ch in word:
              if ch not in node:
                  return False
              node = node[ch]
           retrun self.end_of_word in node 
        
       // 部分匹配
       def startWith(self, prefix:str):
           node = self.root
           for ch in prefix:
               if ch not in node:
                  return False
               node = node[ch]
           retrun True           
             
                       
```

##### <a name="10">208. 实现 Trie (前缀树)</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
```
class Node:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False

    def content_key(self, ch):
        return self.child[ord(ch) - ord('a')]

    def put(self, ch):
        self.child[ord(ch) - ord('a')] = Node()

    def get(self, ch):
        return self.child[ord(ch) - ord('a')]



class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for ch in word:
            if not p.content_key(ch):
                p.put(ch)
            p = p.get(ch)
        p.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for ch in word:
            if p.content_key(ch):
                p = p.get(ch)
            else:
                return False
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for ch in prefix:
            if p.content_key(ch):
                p = p.get(ch)
            else:
                return False
        return True
        
// 第二种方式 字典的形式来存，一层套一层   
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
print(a.search('apple'))
print(a.search('app'))
print(a.startsWith('app'))
a.insert('app')
print(a.search('app'))
print(a.search('apple'))



```
###### <a name="11">208. 实现 Trie (前缀树)感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
// 第一种方法
1.如何返回整个单词
2.如果是插入 ”app“ 和 “apple“ search都会返回true，这是因为每个结点都有一个isEnd，也就是说 app中第二个p的isEnd为True，apple的e的isEnd也是True。所以，查询他俩，都是存在的。最终是通过isEnd，来拿到search的最终结果的

// 第二种方法
1.其实是一层套一层的字典。结束也是以 是否存在结束标志来判断。

```
##### <a name="12">212. 单词搜索 II</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
```

import collections
dx = [-1,1,0,0]
dy = [0,0,-1,1]
END_OF_WORD = '#'
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words: return []
        self.result = set()

        // Greate tria
        root = collections.defaultdict()
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        // traversal
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board,i,j,'',root)
        return list(self.result) 

    def dfs(self, board, i, j, cur_word,cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        temp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] in cur_dict and board[x][y] != '@':
                self.dfs(board,x,y,cur_word,cur_dict)
        board[i][j] = temp        


```

###### <a name="13">212. 单词搜索 II感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
1.创建trie树
2.遍历搜索
3.深度优先遍历
   1>. 此处有一个剪枝的过程，如果board[i][j]不再root里，则代表，第一个单词就不存在，故无需进行遍历
   2>. 因为有4度，故要先定义x，y的数组
   3>. 在dfs的时候需要存储board[i][j],因为为了避免重复遍历同一字符，需要将遍历过的字符置为@
   
```
##### <a name="14">547. 朋友圈</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
[547. 朋友圈](https://leetcode-cn.com/problems/friend-circles/)
[参考链接](https://leetcode-cn.com/problems/friend-circles/solution/union-find-suan-fa-xiang-jie-by-labuladong/)
// dfs
```
```
// bfs
```
```
// 并查集
```
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
                // 将父结点父给自己
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
```
###### <a name="15">547. 朋友圈感想</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
并查集注意点
1.路径压缩
  1>路径如果不压缩，举个例子
  index  =  0 1 2 3 4 5
  parent = [1,1,0,2,3,4]
  假设只有一个根结点，根结点是1。parent中想找到父结点，如过从最后一个结点开始则需要 索引 5的父结点是4，4的父结点是3，->3->2->0->1。需要遍历 o(n)的长度
  2> 路径压缩
  index  =  0 1 2 3 4 5
  parent = [1,1,1,1,1,1]
  将有连系的结点的结点的结点直接置为最顶部的父结点
 2.for循环的时候 
 for i in range(self.n):
            for j in range(i + 1,self.n):
                if M[i][j] == 1:
                    self.union(self.parent, i, j)
 j从 i+1开始是因为每个元素都是双向关系。比如 M[1][2] = 1 代表第2个人和第                     3个人是朋友，相反，第三个人和第二个人也是朋友，所以 M[2][1] = 1页成立。故，遍历一个倒三角即可！！！
3.def find(parents, x):
            while x != parents[x]:
                temp = parents[x]
                // 将父结点父给自己
                parents[x] = parents[temp]
                x = temp
            return x
            
```
##### <a name="16">括号的生成</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
// DP
```
```
// dfs
```
```
##### <a name="17">八皇后</a><a style="float:right;text-decoration:none;" href="#index">[Top]</a>
```
```


