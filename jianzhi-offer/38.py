class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        used = [False]*n
        ret = []

        def helper(combination):
            if len(combination) == len(s):
                ret.append(combination[:])
                return

            for idx, i in enumerate(s):
                if not used[idx]:
                    used[idx] = True
                    helper(combination+i)
                    used[idx] = False

        helper('')
        return list(set(ret))
