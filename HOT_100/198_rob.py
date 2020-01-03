class Solution:
    # dp
    # dp[n] = max(dp[n-2]+nums[n], dp[n-1])
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            pre, cur = cur, max(pre+i, cur)
        return cur


# 扩展 [213]打家劫舍II
'''
唯一变化是成了环状，可以考虑分解成两个子问题
1.不偷第一家
2.不偷最后一家
最终解为 情况1和情况2 的最大值
'''


class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            pre = cur = 0
            for i in nums:
                pre, cur = cur, max(pre+i, cur)
            return cur

        return max(helper(nums[1:]), helper(nums[:-1])) if len(nums) != 1 else nums[0]
