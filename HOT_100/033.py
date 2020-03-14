class Solution:
    # O(logn) 二分，核心是判断如何分数据
    # 检查的时候判断特殊情况：如空List，一个数的list，两个数的list
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target:
                return middle
            # 这里判断需要加=号，middle可能是left
            if nums[middle] >= nums[left]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([3, 1], 1))
