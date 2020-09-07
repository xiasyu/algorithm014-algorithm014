class TreeNode:
    def __init__(self, x:int):
        self.val = x;
        self.left = None
        self.right = None

from typing import List
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level = []
        queue = collections.deque()
        queue.append(root)
        dummy = TreeNode(-1)
        queue.append(dummy)

        while len(queue) != 0:
            node = queue.popleft()
            if node == dummy:
                res.append(level)
                level = []
                if len(queue) != 0:
                    queue.append(dummy)
            else:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    # # 层序遍历
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #
    #     res = []
    #     self.levelOrderHelper(root,0,res)
    #     return res
    #
    # def levelOrderHelper(self, node: TreeNode, level: int, res: List[int]):
    #     if len(res) == level:
    #         res.append([])
    #     res[level].append(node.val)
    #
    #     if node.left:
    #         self.levelOrderHelper(node.left,level + 1,res)
    #     if node.right:
    #         self.levelOrderHelper(node.right, level + 1, res)

    # 前中序创建二叉树
    def buildTree(self, preorder:List[int], inorder:List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        if len(preorder) != len(inorder):
            return None

        n = len(preorder)

        dict = {}
        for i in range(n):
            dict[inorder[i]] = i
        return self.buildTreeHelper(preorder,0,n - 1, 0, n - 1,dict)

    # 创建二叉树帮助
    def buildTreeHelper(self,preorder:List[int], pre_left: int, pre_right: int, in_left: int, in_right: int, dict: {}) -> TreeNode:

        if pre_left > pre_right or in_left > in_right:
            return None

        rootValue = preorder[pre_left]
        index_root = dict[rootValue]
        root = TreeNode(rootValue)

        root.left = self.buildTreeHelper(preorder,pre_left + 1,index_root - in_left + pre_left, in_left, index_root - 1,dict)
        root.right = self.buildTreeHelper(preorder, index_root - in_left + pre_left + 1, pre_right, index_root + 1, in_right,
                                         dict)
        return root

a = Solution()
root = a.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(a.levelOrder(root))

