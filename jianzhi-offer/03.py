class Solution:
    # O(nlogn)
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for idx in range(1, len(nums)):
            if nums[idx-1] == nums[idx]:
                return nums[idx]

    # hash O(n) space O(n)
    def findRepeatNumber2(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                return i

    # index O(n) space o(1)
    def findRepeatNumber3(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return
