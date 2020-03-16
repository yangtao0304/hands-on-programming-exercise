class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = dict()
        for i in nums2:
            while stack and stack[-1] < i:
                val = stack.pop()
                d[val] = i
            stack.append(i)

        res = []
        for i in nums1:
            if i not in d:
                res.append(-1)
            else:
                res.append(d[i])
        return res
