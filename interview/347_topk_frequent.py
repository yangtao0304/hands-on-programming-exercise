class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        from collections import Counter
        c = Counter(nums)
        q = PriorityQueue()

        for num, time in c.items():
            q.put((-time, num))

        res = []
        for i in range(k):
            _, num = q.get()
            res.append(num)
        return res
