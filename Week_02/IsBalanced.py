import collections
class TreeNode:
    def __init__(self,x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 判断是否是平衡二叉树
    def isBalanced(self, root: TreeNode) -> bool:


        return root.val

    # 创建二叉树
    def createBinary(self) -> TreeNode:

        treeNode1 = TreeNode(1)
        treeNode2 = TreeNode(2)
        treeNode3 = TreeNode(3)
        treeNode4 = TreeNode(4)
        treeNode5 = TreeNode(5)
        treeNode6 = TreeNode(6)

        treeNode1.left = treeNode2
        treeNode1.right = treeNode3
        treeNode2.left = treeNode4
        treeNode2.right = treeNode5
        treeNode3.left = treeNode6

        return  treeNode1

    # 二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque()
        queue.append(root)
        res = 0
        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            res += 1

        return res

a = Solution()
treeNode = a.createBinary()
print(a.maxDepth(treeNode))
