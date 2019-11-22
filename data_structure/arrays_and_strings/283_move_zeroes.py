class Solution(object):
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[i] = nums[idx]
                i += 1
        for idx in range(i, len(nums)):
            nums[idx] = 0

    def move_zeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                # swap
                nums[i], nums[idx] = nums[idx], nums[i]
                i += 1
