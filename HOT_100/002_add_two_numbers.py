'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 循环 1
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        p_pre = ListNode(None)
        p = p_pre
        carry = 0

        while p1 and p2:
            num_sum = p1.val + p2.val + carry
            carry = num_sum // 10
            p.next = ListNode(num_sum % 10)
            p = p.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            num_sum = p1.val + carry
            p.next = ListNode(num_sum % 10)
            p = p.next
            carry = num_sum // 10
            p1 = p1.next

        while p2:
            num_sum = p2.val + carry
            p.next = ListNode(num_sum % 10)
            p = p.next
            carry = num_sum // 10
            p2 = p2.next

        if carry:
            p.next = ListNode(1)

        return p_pre.next

    # 循环 2
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        p_pre = ListNode(None)
        p = p_pre
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            num_sum = x + y + carry
            p.next = ListNode(num_sum % 10)
            p = p.next
            carry = num_sum // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            p.next = ListNode(1)
        return p_pre.next

    # 递归
    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        val = l1.val + l2.val
        node = ListNode(val % 10)
        node.next = self.addTwoNumbers3(l1.next, l2.next)

        if val >= 10:
            node.next = self.addTwoNumbers3(node.next, ListNode(1))

        return node
