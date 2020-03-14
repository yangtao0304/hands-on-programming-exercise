class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(first=0):
            if first == len(nums)-1:
                res.append(nums[:])
            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                helper(first+1)
                nums[i], nums[first] = nums[first], nums[i]
        res = []
        helper()
        return res
