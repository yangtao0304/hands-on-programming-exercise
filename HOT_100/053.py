# 连续最大子序列和

# [-2,1,-3,4,-1,2,1,-5,4], 6
#  连续子数组 [4,-1,2,1] 的和最大，为 6


class Solution:
    # 贪心法
    # 每一步都选择最佳方案，到最后就是全局最优的方案
    def maxSubArray(self, nums):
        if not nums:
            return
        max_sum = tmp = nums[0]
        for num in nums[1:]:
            tmp = max(num, tmp + num)
            max_sum = max(tmp, max_sum)
        return max_sum

    # 动态规划（Kadane 算法）
    # 当前最大连续子序列和为 sum，结果为 ans
    # 如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
    # 如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
    # 每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
    # 时间复杂度：O(n)
    def maxSubArray2(self, nums):
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)
        return max_sum

    # 分治法
    def maxSubArray3(self, nums):
        pass


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray2(nums))
    print(nums)
