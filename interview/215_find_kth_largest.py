class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1

        def sort(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = partition(lo, hi)
            if mid == len(nums)-k:
                return nums[mid]
            elif mid < len(nums)-k:
                return sort(mid+1, hi)
            else:
                return sort(lo, mid-1)

        def partition(lo, hi):
            pivot = nums[hi]
            loc = lo-1
            for i in range(lo, hi):
                if nums[i] < pivot:
                    loc += 1
                    # swap
                    nums[loc], nums[i] = nums[i], nums[loc]
            nums[loc+1], nums[hi] = nums[hi], nums[loc+1]
            return loc+1

        return sort(lo, hi)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
