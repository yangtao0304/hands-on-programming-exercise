# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 迭代 三指针
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    # 递归 比较难理解！
    def reverseList2(self, head: ListNode) -> ListNode:
        # 特判
        if head == None:
            return head

        # 开始递归
        if head.next == None:
            return head

        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None

        return p
