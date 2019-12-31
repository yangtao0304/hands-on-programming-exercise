'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例：

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for i in range(len(nums)):
            if i < d[0]:
                nums[i] = 0
            elif i < d[0]+d[1]:
                nums[i] = 1
            else:
                nums[i] = 2

    # 双指针 O(n)
    def sortColors2(self, nums: List[int]) -> None:
        left = 0
        right = len(nums)-1
        # index 指 最右0值的下标+1
        index = 0
        # while判断若不加等号，bad case：[2,0,1]
        while left <= right:
            if nums[left] == 2:
                # swap left, right
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            elif nums[left] == 0:
                # swap left,index
                nums[left], nums[index] = nums[index], nums[left]
                index += 1
                left += 1
            else:
                left += 1
