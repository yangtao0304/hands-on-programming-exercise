from typing import List


class Solution:
    # 查找一个数
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n-1
        while left <= right:
            mid = (right-left)//2+left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

    # 查找左边界
    def search2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n
        # 左闭右空 [left,right)
        while left < right:
            mid = (right-left)//2+left
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1

        return left

    # 查找右边界
    def search3(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n
        # 左闭右空 [left,right)
        while left < right:
            mid = (right-left)//2+left
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid

        return left-1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search2([1, 2, 2, 2, 3], 2))
    print(s.search3([1, 2, 2, 2, 3], 2))
