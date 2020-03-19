# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''


class Solution:
    # 扫描两躺
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 引入哑节点来简化某些极端情况：如只有一个节点或者要删除头节点
        dummy = ListNode(None)
        dummy.next = head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        length -= n
        first = dummy
        for i in range(length):
            first = first.next
        first.next = first.next.next
        return dummy.next

    # 扫描一躺
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        first = dummy
        for i in range(n):
            first = first.next
        last = dummy
        while first.next:
            first = first.next
            last = last.next
        last.next = last.next.next
        return dummy.next
