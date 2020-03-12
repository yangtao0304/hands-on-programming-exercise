# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return cur
