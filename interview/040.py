class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        is_used = [False]*len(candidates)

        def backtrack(target, combination):
            if target == 0:
                res.append(combination[:])
            for idx, num in enumerate(candidates):
                if num <= target and not is_used[idx] and (not combination or combination[-1] <= num):
                    is_used[idx] = True
                    backtrack(target-num, combination+[num])
                    is_used[idx] = False
        backtrack(target, [])
        ret = [list(_) for _ in set(tuple(i) for i in res)]
        return ret
