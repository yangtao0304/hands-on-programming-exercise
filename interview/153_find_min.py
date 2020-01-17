class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        left = 0
        right = n-1
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (right-left)//2+left
            # 顺序最好不要反过来
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[left]:
                left = mid+1
            else:
                right = mid-1


if __name__ == "__main__":
    s = Solution()
    res = s.findMin([5, 1, 2, 3, 4])
    print(res)
