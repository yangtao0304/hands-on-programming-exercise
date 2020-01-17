class Solution:
    # 排序
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left_idx = 0
        right_idx = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left_idx = i
                break

        for i in reversed(range(len(nums))):
            if nums[i] != sorted_nums[i]:
                right_idx = i
                break
        return right_idx-left_idx+1

    # stack

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        stack = []
        left_idx = len(nums)
        for idx in range(len(nums)):
            if not stack or nums[idx] >= nums[stack[-1]]:
                stack.append(idx)
            else:
                while stack and nums[idx] < nums[stack[-1]]:
                    tmp = stack.pop()
                    left_idx = min(tmp, left_idx)
                stack.append(idx)

        stack2 = []
        right_idx = -1
        for idx in reversed(range(len(nums))):
            if not stack2 or nums[idx] <= nums[stack2[-1]]:
                stack2.append(idx)
            else:
                while stack2 and nums[idx] > nums[stack2[-1]]:
                    tmp = stack2.pop()
                    right_idx = max(tmp, right_idx)
                stack2.append(idx)

        return right_idx-left_idx+1 if right_idx != -1 else 0
