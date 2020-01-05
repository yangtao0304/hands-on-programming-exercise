# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # reverse作用是：反转m-n 和 与后一部分连接
        def reverse(head, m, n):
            prev = None
            cur = head
            next = None
            for i in range(n-m+1):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            head.next = cur
            return prev

        # m=1，直接调用
        if m == 1:
            return reverse(head, m, n)

        # 找到m所在的节点和它的前一个节点
        prev = None
        cur = head
        for i in range(m-1):
            prev = cur
            cur = cur.next

        reversed_head = reverse(cur, m, n)
        # 与前一部分连接
        prev.next = reversed_head

        return head
