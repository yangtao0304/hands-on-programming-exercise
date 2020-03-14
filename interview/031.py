class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        size = len(nums)
        idx_a, idx_b = -1, -1
        for i in reversed(range(1, size)):
            if nums[i] > nums[i-1]:
                idx_a = i-1
                break

        if idx_a == -1:
            reverse(nums, 0)
        else:
            for i in reversed(range(1, size)):
                if nums[i] > nums[idx_a]:
                    idx_b = i
                    break
            # swap
            nums[idx_a], nums[idx_b] = nums[idx_b], nums[idx_a]
            reverse(nums, idx_a+1)
