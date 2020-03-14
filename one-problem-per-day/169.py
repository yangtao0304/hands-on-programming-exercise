class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for i in nums[1:]:
            if i == major:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    major = i
        return major
