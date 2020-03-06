class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        res = []
        from collections import deque
        q = deque()

        # initialize
        for idx, num in enumerate(nums[:k]):
            while q and num >= nums[q[-1]]:
                q.pop()
            q.append(idx)

        res.append(nums[q[0]])

        l = 0
        for idx, num in enumerate(nums[k:]):
            while q and num >= nums[q[-1]]:
                q.pop()
            q.append(idx+k)

            if q[0] <= l:
                q.popleft()
            res.append(nums[q[0]])
            l += 1
        return res
