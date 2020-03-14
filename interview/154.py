class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if len(set(nums)) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = n-1
        while l < r:
            mid = (r-l)//2+l
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]
