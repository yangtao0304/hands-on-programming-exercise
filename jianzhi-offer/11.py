class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if len(set(numbers)) == 1:
            return numbers[0]

        if numbers[0] < numbers[-1]:
            return numbers[0]

        l = 0
        r = n-1
        while l < r:
            mid = (r-l)//2+l
            if numbers[mid] > numbers[r]:
                l = mid+1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]
