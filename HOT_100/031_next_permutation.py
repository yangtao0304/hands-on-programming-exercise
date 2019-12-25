# 暴力解决需要O(n!)
'''
字典序算法步骤：1.从右向左，找出第一个左边小于右边的数，记为a
             2.从右向左，找出第一个大于a的数，记为b
             3.交换a,b
             4.将原先a位置后的数从小到大排列（逆序）
'''


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        size = len(nums)
        idx_a, idx_b = -1, -1
        for i in reversed(range(1, size)):
            if nums[i] > nums[i-1]:
                idx_a = i-1
                break

        if idx_a == -1:
            reverse(nums, 0)
        else:
            for i in reversed(range(1, size)):
                if nums[i] > nums[idx_a]:
                    idx_b = i
                    break
            # swap
            nums[idx_a], nums[idx_b] = nums[idx_b], nums[idx_a]
            reverse(nums, idx_a+1)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    print(nums)
