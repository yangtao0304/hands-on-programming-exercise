class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        is_appear = [False]*14

        min_num = 14
        max_num = -1
        for i in nums:
            if i == 0:
                continue
            elif is_appear[i] == True:
                return False
            is_appear[i] = True
            min_num = min(min_num, i)
            max_num = max(max_num, i)

        return max_num-min_num+1 <= 5
