class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        each = len(candies)//2
        s = set()
        for i in candies:
            s.add(i)
        return min(each, len(s))
