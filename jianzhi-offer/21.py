class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        while l < r:
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
