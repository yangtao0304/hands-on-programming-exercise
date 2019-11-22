class Solution(object):
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # given nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        # return [0, 1, 2, 3, 4]

        i = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx-1]:
                i += 1
                nums[i] = nums[idx]
        return i+1

    def remove_duplicates_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # given nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        # return [0, 1, 2, 3, 4]

        i = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[i]:
                i += 1
                nums[i] = nums[idx]
        return i+1

    def removeDuplicates_3(self, nums):
        for num_index in range(len(nums)-1, 0, -1):
            if nums[num_index] == nums[num_index-1]:
                nums.pop(num_index)
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.remove_duplicates([1, 1, 2, 3, 3, 2]))
