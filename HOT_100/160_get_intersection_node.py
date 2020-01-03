# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # O(m+n) O(m)/O(n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a = headA
        s_a = set()
        while cur_a:
            s_a.add(cur_a)
            cur_a = cur_a.next

        cur_b = headB
        while cur_b:
            if cur_b in s_a:
                return cur_b
            cur_b = cur_b.next
        return None

    # 双指针法
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        p1 = headA
        p2 = headB
        count_1 = count_2 = True

        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if not p1:
                if count_1:
                    p1 = headB
                    count_1 = False
                else:
                    break
            if not p2:
                if count_2:
                    p2 = headA
                    count_2 = False
                else:
                    break

        return None

    # 双指针 精简版
    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        p1 = headA
        p2 = headB
        # 循环退出时的状态
        # 1.找到相交；or 2.为null
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1

    # 长度相减
    def getIntersectionNode4(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        c1, c2 = 0, 0
        p1 = headA
        p2 = headB
        while p1.next:
            p1 = p1.next
            c1 += 1
        while p2.next:
            p2 = p2.next
            c2 += 1

        # 判断是否相交
        if p1 != p2:
            return None

        p1 = headA
        p2 = headB
        if c1 <= c2:
            k = c2-c1
            for i in range(k):
                p2 = p2.next
        else:
            k = c1-c2
            for i in range(k):
                p1 = p1.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
