'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5, 7, 7, 8, 8, 10], target = 8
输出: [3, 4]
示例 2:

输入: nums = [5, 7, 7, 8, 8, 10], target = 6
输出: [-1, -1]
'''


class Solution:
    # 判断最左或者最右的时候，要考虑到边界问题
    def searchRange(self, nums, target):
        res = [-1, -1]
        # find left
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target and (middle-1 < 0 or nums[middle-1] != target):
                res[0] = middle
                break
            elif nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1

        # find right
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target and (middle+1 >= len(nums) or nums[middle+1] != target):
                res[1] = middle
                break
            elif nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1], 1))
