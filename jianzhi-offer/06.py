# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        phead = head
        while phead:
            stack.append(phead.val)
            phead = phead.next
        return stack[::-1]

    def reversePrint2(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        return self.reversePrint(head.next)+[head.val]
