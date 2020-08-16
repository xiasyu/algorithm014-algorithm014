# [24.两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
class ListNode:
    def __init___(self,x):
        self.val = x
        self.next = None



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        print('gello world')

    from typing import List
    def createListMode(val: List[int]) -> ListNode:

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next



a = Solution()
a.swapPairs(ListNode())