from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums:
            return res

        # initialize
        from collections import deque
        q = deque()
        for idx, num in enumerate(nums[:k]):
            while q and num >= nums[q[-1]]:
                q.pop()
            q.append(idx)

        res.append(nums[q[0]])

        l = 1
        for idx, num in enumerate(nums[k:]):
            while q and num >= nums[q[-1]]:
                q.pop()
            # +k 容易忽略掉
            q.append(idx+k)

            if q[0] < l:
                q.popleft()
            res.append(nums[q[0]])
            l += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
