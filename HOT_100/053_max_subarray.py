# 连续最大子序列和

# [-2,1,-3,4,-1,2,1,-5,4], 6
#  连续子数组 [4,-1,2,1] 的和最大，为 6


class Solution:
    # 贪心法
    # 每一步都选择最佳方案，到最后就是全局最优的方案
    def maxSubArray(self, nums):
        if not nums:
            return 0
        max_sum = tmp = nums[0]
        for num in nums[1:]:
            tmp = max(num, tmp + num)
            max_sum = max(tmp, max_sum)
        return max_sum

    # 动态规划（Kadane 算法）
    def maxSubArray2(self, nums):
        pass

    # 分治法
    def maxSubArray3(self, nums):
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
