# [21.合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
# 定义一个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 定义一个单链表
class LinkList:
    def __init__(self):
        self.head = None

    def initList(self,data) -> ListNode:
        #创建头节点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为data内的数据创建节点，建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return  r

    # 输出一个链表
    def printList(self, head: ListNode):
        if head == None:
            return
        node = head
        while node:
            print(node.val)
            node = node.next

    # 1、 合并两个有序链表 (使用迭代)
    def mergeTwoListsIteration(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev_node = dummy
        while (l1 is not None) & (l2 is not None):
            if l1.val < l2.val:
                prev_node.next = l1
                l1 = l1.next
            else:
                prev_node.next = l2
                l2 = l2.next
            prev_node = prev_node.next
        if l1 is not None:
            prev_node.next = l1
        else:
            prev_node.next = l2

        return dummy.next


    # 2、使用递归
    def mergeTwoListsRecursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursion(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursion(l1,l2.next)
            return l2




# 初始化链表
l1 = LinkList()
# 创建一个链表
l1.initList([1,3,5,7,9])

# # 输出一个链表
# l1.printList(l1.head)


# 初始化第二个链表
l2 = LinkList()
# 创建第二个链表
l2.initList([2,4,6,8,10])

# # 输出第二个个链表
# l2.printList(l2.head)

# 迭代合并链表
mergeLinkList = LinkList()
# printMergeLinkList1 = mergeLinkList.mergeTwoListsIteration(l1.head,l2.head)
# mergeLinkList.printList(printMergeLinkList1)

# 递归合并链表
printMergeLinkList2 = mergeLinkList.mergeTwoListsRecursion(l1.head,l2.head)
mergeLinkList.printList(printMergeLinkList2)