class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random

        def partition(lo, hi):
            idx = random.randint(lo, hi)
            nums[idx], nums[hi] = nums[hi], nums[idx]
            pivot = nums[hi]
            loc = lo-1
            for i in range(lo, hi):
                if nums[i] < pivot:
                    loc += 1
                    nums[loc], nums[i] = nums[i], nums[loc]
            nums[loc+1], nums[hi] = nums[hi], nums[loc+1]
            return loc+1

        left = 0
        right = len(nums)-1
        pivot = partition(left, right)
        while pivot != len(nums)-k:
            if pivot < len(nums)-k:
                pivot = partition(pivot+1, right)
            elif pivot > len(nums)-k:
                pivot = partition(left, pivot-1)
        return nums[pivot]
