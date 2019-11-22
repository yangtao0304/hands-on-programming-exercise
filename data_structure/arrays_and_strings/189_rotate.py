class Solution(object):
    # 暴力旋转k次 O(n*k)
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k:
            temp = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = temp
            k -= 1

    # 使用额外数组 O(n)+O(n)
    def rotate_2(self, nums, k):
        new_nums = [0]*len(nums)
        for idx in range(len(nums)):
            new_nums[(idx+k) % len(nums)] = nums[idx]
        for i in range(len(nums)):
            nums[i] = new_nums[i]

    # 使用反转
    def rotate_3(self, nums, k):
        '''
        假设 n=7 且 k=3

        原始数组                  : 1 2 3 4 5 6 7
        反转所有数字后             : 7 6 5 4 3 2 1
        反转前 k 个数字后          : 5 6 7 4 3 2 1
        反转后 n-k 个数字后        : 5 6 7 1 2 3 4 --> 结果
        '''
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # 很关键，k可能会大于len(nums)
        k %= len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
