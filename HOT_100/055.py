'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
'''

from typing import List


class Solution:
    # 贪心，从后向前
    # O(n)
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in reversed(range(len(nums)-1)):
            if i+nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0

    # 贪心，从前向后，尽可能到达最远位置
    # O(n)
    def canJump2(self, nums: List[int]) -> bool:
        max_i = 0  # 初始化当前最远能到达位置
        for i, jump in enumerate(nums):
            if max_i < i:
                return False
            else:  # 如果当前位置能到达，并且当前位置+跳数>最大位置，更新最大位置
                max_i = max(max_i, i+jump)
        return True

    # dp O(n^2) 会超时
    def canJump3(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True  # 0位置可达
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] and j+nums[j] >= i:  # 若dp[j]可达，且可从j到i
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.canJump2([2, 3, 1, 1, 4]))
