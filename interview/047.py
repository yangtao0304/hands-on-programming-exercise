class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(first=0):
            if first == len(nums)-1:
                res.append(nums[:])
            s = set()
            for i in range(first, len(nums)):
                if nums[i] in s:
                    continue
                nums[i], nums[first] = nums[first], nums[i]
                helper(first+1)
                nums[i], nums[first] = nums[first], nums[i]
                s.add(nums[i])
        res = []
        helper()
        return res
