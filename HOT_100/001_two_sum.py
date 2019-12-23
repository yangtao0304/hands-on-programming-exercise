class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, num in enumerate(nums):
            if num not in d:
                d[target - num] = idx
            else:
                return [d[num], idx]
