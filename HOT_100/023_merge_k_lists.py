# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 1: 暴力 O(nlogn)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        head = point = ListNode(0)
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    # 2: 逐一比较（使用优先队列优化）
    # 优先级队列可以使用python包的queue.PriorityQueue
    # 实质是使用最小堆heapq来实现的，考虑了线程安全的问题
    # O(nlogk)
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        q = PriorityQueue()
        index = 0
        for l in lists:
            if l:
                q.put((l.val, index, l))
                index += 1
        head = point = ListNode(0)
        while not q.empty():
            val, _, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, index, node))
                index += 1
        return head.next
