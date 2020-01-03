'''
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialize
        max_pro = float('-inf')
        tmp_min = 1
        tmp_max = 1
        
        for i in nums:
            if i < 0:
                tmp_min, tmp_max = tmp_max, tmp_min
            tmp_min = min(tmp_min*i, i)
            tmp_max = max(tmp_max*i, i)
            max_pro = max(max_pro, tmp_max)

        return max_pro
