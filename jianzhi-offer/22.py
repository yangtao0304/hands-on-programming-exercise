# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 1:
            return
        nxt = head
        pre = head
        for i in range(k-1):
            if nxt.next == None:
                return
            nxt = nxt.next

        while nxt.next != None:
            pre = pre.next
            nxt = nxt.next
        return pre
