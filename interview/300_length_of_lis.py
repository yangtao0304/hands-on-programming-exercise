# 最长上升子序列


class Solution(object):
    # dp
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        print(dp)
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    s.lengthOfLIS([4, 10, 4, 3, 8, 9])
