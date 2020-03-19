class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(target, combination):
            if target == 0:
                res.append(combination[:])
                return
            for i in candidates:
                if i <= target and (not combination or i >= combination[-1]):
                    backtrack(target-i, combination+[i])
        backtrack(target, [])
        return res
