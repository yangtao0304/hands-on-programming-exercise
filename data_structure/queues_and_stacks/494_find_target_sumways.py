from typing import List


class Solution:
    # 暴力解法
    # 组合个数为2^n
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(nums, target, idx):
            if idx == len(nums):
                return 1 if target == 0 else 0
            ans = 0
            # 对应加的情况
            ans += dfs(nums, target-nums[idx], idx+1)
            # 对应减的情况
            ans += dfs(nums, target+nums[idx], idx+1)
            return ans

        return dfs(nums, S, 0)

    # 01背包 to be implemented
    # https://leetcode-cn.com/problems/target-sum/solution/c-dfshe-01bei-bao-by-bao-bao-ke-guai-liao/
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    res = s.findTargetSumWays(
        [27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0], 10)
    print(res)
