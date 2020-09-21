import collections

from typing import List
# 层序遍历
def preorder(self, root: 'Node') -> List[int]:
    if root == None:
        return []
    q = collections.deque()
    q.append(root)
    res = []
    while len(q) != 0:
        node = q.popleft()
        res.append(node.val)
        if node.children:
            q.extend(node.children[::-1])
    return res

