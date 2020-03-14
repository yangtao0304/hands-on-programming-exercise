class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0]*n
        stack = []
        for idx, temp in enumerate(T):
            if not stack or T[stack[-1]] >= temp:
                stack.append(idx)
            else:
                while stack and T[stack[-1]] < temp:
                    tmp_idx = stack.pop()
                    res[tmp_idx] = idx-tmp_idx
                stack.append(idx)
        return res
