# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummpy = ListNode(0)
        dummpy.next = head

        pre = dummpy
        cur = dummpy.next

        while True:
            if cur.val == val:
                pre.next = cur.next
                break

            pre = pre.next
            cur = cur.next

        return dummpy.next
