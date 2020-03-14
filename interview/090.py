class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(i, tmp):
            res.append(tmp[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                helper(j+1, tmp+[nums[j]])
        helper(0, [])
        return res
