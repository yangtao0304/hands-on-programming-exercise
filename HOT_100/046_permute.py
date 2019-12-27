from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return [[]]
        n = 1
        for i in range(1, size+1):
            n *= i

        nums.sort()
        res = [nums.copy()]
        while n-1:
            idx_a, idx_b = 0, 0
            for i in range(size-1, 0, -1):
                if nums[i] > nums[i-1]:
                    idx_a = i-1
                    break
            for i in range(size-1, -1, -1):
                if nums[i] > nums[idx_a]:
                    idx_b = i
                    break
            nums[idx_a], nums[idx_b] = nums[idx_b], nums[idx_a]

            left = idx_a+1
            right = size-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

            res.append(nums.copy())
            n -= 1

        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return [[]]
        n = 1
        for i in range(1, size+1):
            n *= i

        res = [nums.copy()]

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        while n-1:
            idx_a, idx_b = -1, 0
            for i in range(size-1, 0, -1):
                if nums[i] > nums[i-1]:
                    idx_a = i-1
                    break
            for i in range(size-1, -1, -1):
                if nums[i] > nums[idx_a]:
                    idx_b = i
                    break

            if idx_a == -1:
                reverse(0, size-1)
            else:
                nums[idx_a], nums[idx_b] = nums[idx_b], nums[idx_a]
                reverse(idx_a+1, size-1)

            res.append(nums.copy())
            n -= 1

        return res

    def permute3(self, nums: List[int]) -> List[List[int]]:

        def backtrack(combination, nexts):
            if len(nexts) == 0:
                res.append(combination)
            else:
                for i in nexts:
                    tmp = nexts.copy()
                    tmp.remove(i)
                    backtrack(combination+[i], tmp)

        res = []
        if nums:
            backtrack([], nums)
        return res

    def permute4(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # swap i, first
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.permute3([1, 2, 3]))
