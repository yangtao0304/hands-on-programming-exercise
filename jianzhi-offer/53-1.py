class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # find left
        left = 0
        right = n-1
        left_idx = -1
        while left <= right:
            mid = (right-left)//2+left
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                left_idx = mid
                break
            elif nums[mid] >= target:
                right -= 1
            else:
                left += 1

        # find right
        left = 0
        right = n-1
        right_idx = -2
        while left <= right:
            mid = (right-left)//2+left
            if nums[mid] == target and (mid == n-1 or nums[mid+1] != target):
                right_idx = mid
                break
            elif nums[mid] <= target:
                left += 1
            else:
                right -= 1

        return right_idx-left_idx+1
