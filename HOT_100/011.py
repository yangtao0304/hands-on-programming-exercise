# 盛最多水的容器


class Solution:
    # 方法一：暴力，方法二：双指针
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
