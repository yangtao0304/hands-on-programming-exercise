class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l = 1
        r = 2
        res = []
        while l < r:
            s = (r+l)*(r-l+1)//2
            if s == target:
                res.append([i for i in range(l, r+1)])
                print(res)
                l += 1
            elif s < target:
                r += 1
            else:
                l += 1
        return res
