# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # O(n) O(n)
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        s = set()
        while cur:
            if cur not in s:
                s.add(cur)
                cur = cur.next
            else:
                return cur

        return None

    # 快慢指针
    def detectCycle2(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None

        cur = head
        slow = cur
        fast = cur.next

        # while退出时候的slow并不是环形链表的入口
        while slow != fast:
            # 判断是否无环，无环直接返回
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next

        # 有环
        # 计算环的大小

        tmp = slow.next
        length = 1
        while tmp != slow:
            tmp = tmp.next
            length += 1

        p1 = p2 = head
        for i in range(length):
            p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
