class Solution(object):
    def dominant_index(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_idx = nums.index(max(nums))
        for idx, x in enumerate(nums):
            if idx != max_idx:
                if nums[max_idx] < 2*x:
                    return -1
        return max_idx

    def dominantIndex(self, nums):
        '''
        any(iterable, /)
            Return True if bool(x) is True for any x in the iterable.
            
            If the iterable is empty, return False.
        all(iterable, /)
            Return True if bool(x) is True for all values x in the iterable.
            
            If the iterable is empty, return True.
        '''
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1
