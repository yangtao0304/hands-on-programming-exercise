# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 哈希表
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head not in s:
                s.add(head)
            else:
                return True
            head = head.next
        return False

    # 快慢指针
    def hasCycle2(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
