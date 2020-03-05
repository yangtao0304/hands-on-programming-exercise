class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]
        for i in nums[1:]:
            if i == major:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    count = 1
                    major = i
        return major
