class Solution(object):
    def pivot_index(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return -1
        left = 0
        right = sum(nums[1:])
        if right == 0:
            return 0
        for idx in range(1, length):
            left += nums[idx-1]
            right -= nums[idx]
            if left == right:
                return idx
        return -1

    def pivotIndex(self, nums):
        # left_sum == S - left_sum - nums[i]
        S = sum(nums)
        left_sum = 0
        for idx, x in enumerate(nums):
            if left_sum == S-left_sum-x:
                return idx
            left_sum += x
        return -1
