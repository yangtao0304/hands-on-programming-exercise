class Solution(object):
    def min_subarray_len(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        p_1 = p_2 = 0
        min_len = nums_len
        while p_1 <= p_2 and p_2 < nums_len:
            # 达到条件 <-> 破坏条件
            if sum(nums[p_1:p_2+1]) >= s:
                length = p_2-p_1+1
                min_len = min(min_len, length)
                p_1 += 1
            else:
                p_2 += 1

        if min_len == nums_len and sum(nums) < s:
            min_len = 0
        return min_len

if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7,[2,3,1,2,4,3]))