# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 1: 暴力 O(nlogn)
    # 这里，n为k个链表中所有节点个数和
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        head = cur = ListNode(0)
        for x in sorted(vals):
            cur.next = ListNode(x)
            cur = cur.next
        return head.next

    # 2: 逐一比较（使用优先队列优化）
    # k路归并
    # 优先级队列可以使用python包的queue.PriorityQueue
    # 实质是使用最小堆heapq来实现的，考虑了线程安全的问题
    # O(nlogk) 空间O(n),因为新建链表保存结果
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        q = PriorityQueue()
        index = 0
        for l in lists:
            if l:
                q.put((l.val, index, l))
                index += 1
        head = cur = ListNode(0)
        while not q.empty():
            val, _, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, index, node))
                index += 1
        return head.next

    # 分治递归 O(nlogk) 空间O(1)
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:

        def split_two(left, right):
            # 递归终止
            if left == right:
                return lists[left]
            mid = (right-left)//2+left
            return merge(split_two(left, mid), split_two(mid+1, right))

        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val <= l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        return split_two(0, len(lists)-1)
