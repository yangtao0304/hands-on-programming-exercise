from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0

        def merge_sort(nums, left, right):
            if left < right:
                mid = (right-left)//2+left
                merge_sort(nums, left, mid)
                merge_sort(nums, mid+1, right)
                merge(nums, left, mid, right)

        def merge(nums, left, mid, right):
            tmp = [0]*(right-left+1)
            a = left
            b = mid+1
            nonlocal count
            for k in range(len(tmp)):
                if a > mid:
                    tmp[k] = nums[b]
                    b += 1
                elif b > right:
                    tmp[k] = nums[a]
                    a += 1
                elif nums[a] > nums[b]:
                    tmp[k] = nums[b]
                    b += 1
                    count += (mid-a+1)
                else:
                    tmp[k] = nums[a]
                    a += 1
            for i in range(len(tmp)):
                nums[left+i]=tmp[i]

        merge_sort(nums, 0, len(nums)-1)
        # print(nums)
        return count


if __name__ == "__main__":
    s = Solution()
    count = s.reversePairs([7, 5, 6, 4])
    print(count)
