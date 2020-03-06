class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []

        left = 0
        right = len(nums)-1

        while left < right:
            if nums[left]+nums[right] < target:
                left += 1
            elif nums[left]+nums[right] > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
