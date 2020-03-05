class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right-left)//2+left
            if nums[mid] == mid:
                left = mid+1
            else:
                if mid == 0 or nums[mid-1] == mid-1:
                    return mid
                else:
                    right = mid-1
        # case
        # input [0,1], return 2
        return len(nums)
