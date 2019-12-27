'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

# 递归 + 回溯
from typing import List


class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(combination, remain):
            if remain == 0:
                outputs.append(combination)
            else:
                for i in candidates:
                    if i <= remain and (not combination or i >= combination[-1]):
                        backtrack(combination+[i], remain-i)

        outputs = []
        backtrack([], target)
        return outputs

    # 回溯 + 剪枝
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        tmp_path = []
        outputs = []

        def traceback(tmp_path, target, start):
            if target < 0:
                return
            if target == 0:
                outputs.append(tmp_path.copy())
                return
            for i in range(start, n):
                tmp_path.append(candidates[i])
                traceback(tmp_path, target-candidates[i], i)
                tmp_path.pop()

        traceback(tmp_path, target, 0)
        return outputs

    def combinationSum3(self, candidates, target):
        n = len(candidates)
        tmp_path = []
        outputs = []
        candidates.sort()

        def traceback(tmp_path, target, start):
            if target < 0:
                return
            if target == 0:
                outputs.append(tmp_path.copy())
                return
            for i in range(start, n):
                if target < candidates[i]:
                    break
                tmp_path.append(candidates[i])
                traceback(tmp_path, target-candidates[i], i)
                tmp_path.pop()

        traceback(tmp_path, target, 0)
        return outputs

    # 动态规划求解：https://leetcode-cn.com/problems/combination-sum/solution/chao-qiang-gifzhu-ni-shi-yong-dong-tai-gui-hua-qiu/
    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        dict = {}
        for i in range(1, target+1):
            dict[i] = []

        for i in range(1, target+1):
            for j in candidates:
                if j == i:
                    dict[i].append([j])
                elif i > j:
                    for k in dict[i-j]:
                        k = k.copy()
                        k.append(j)
                        k.sort()
                        if k not in dict[i]:
                            dict[i].append(k)

        return dict[target]


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([5, 3, 2], 8))
    print(s.combinationSum4([5, 3, 2], 8))
