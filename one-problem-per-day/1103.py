class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        i = 0
        num = 1
        while candies:
            tmp = min(num, candies)
            res[i] += tmp
            candies -= tmp
            i = (i+1) % num_people
            num += 1
        return res
