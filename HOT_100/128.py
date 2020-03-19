'''
给定一个未排序的整数数组，找出最长连续序列的长度
要求算法的时间复杂度为 O(n)

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4
'''


class Solution:
    # 暴力 O(n^2)
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        for i in nums:
            cur_num = i
            cur_len = 1
            while cur_num + 1 in nums:
                cur_num += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len

    # 排序 O(nlogn)
    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        max_len = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
        return max(max_len, cur_len)

    # hash table O(n)

    def longestConsecutive3(self, nums: List[int]) -> int:
        max_len = 0
        set_nums = set(nums)

        for i in set_nums:
            if i-1 not in set_nums:
                cur_num = i
                cur_len = 1
                while cur_num+1 in set_nums:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)

        return max_len
