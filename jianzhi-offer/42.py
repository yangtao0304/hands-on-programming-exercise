class Solution:
    # greedy
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = max_num = nums[0]
        for i in nums[1:]:
            tmp = max(tmp+i, i)
            max_num = max(tmp, max_num)
        return max_num

    # dp
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_num = max(max_num, nums[i])
        return max_num
