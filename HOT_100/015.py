'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        size = len(nums)
        res = []
        if size < 3:
            return res

        nums.sort()

        for i in range(size):
            if nums[i] > 0:
                return res

            # 这一个判断可以去除重复
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i]+nums[left]+nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
