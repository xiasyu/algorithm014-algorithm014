
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    # 反序遍历
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        self.helper(head, res)
        res = res[::-1]
        return res

    def helper(self, head: ListNode, res: List[int]):
        # recursion terminator
        if head == None:
            return res

        # process login in current level
        res.append(head.val)

        # drill down
        self.helper(head.next, res)

        # reverse the current status if needed

    # 创建链表
    def createListMode(self,nums:List[int]) -> ListNode:
        if len(nums) == 0:
            return None
        tempListNode = ListNode(-1)
        head = ListNode(nums[0])
        tempListNode.next = head
        for i in range(1,len(nums)):
            head.next = ListNode(nums[i])
            head = head.next

        return tempListNode.next
a = Solution()
head = a.createListMode([1,3,2,9,10])
print(head)
print(a.reversePrint(head))


