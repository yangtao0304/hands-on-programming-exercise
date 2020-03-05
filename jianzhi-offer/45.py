class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums:
            return None

        nums = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] > nums[j]+nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)
