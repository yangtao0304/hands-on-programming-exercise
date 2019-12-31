'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

'''
from typing import List


class Solution:
    # 暴力 O(n^3)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            for j in range(i, n):
                min_height = float('inf')
                for k in range(i, j+1):
                    min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height*(j-i+1))
        return max_area

    # 暴力，对方法1进行优化 O(n^2)
    def largestRectangleArea2(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            min_height = float('inf')
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height*(j-i+1))
        return max_area

    # 分治 平均 O(nlogn) 最坏 O(n^2),当heights是有序时
    def largestRectangleArea3(self, heights: List[int]) -> int:
        def cal_area(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for idx in range(start+1, end+1):
                if heights[min_index] > heights[idx]:
                    min_index = idx
            return max(heights[min_index]*(end-start+1), cal_area(heights, start, min_index-1), cal_area(heights, min_index+1, end))

        return cal_area(heights, 0, len(heights)-1)

    # 栈 O(n)
    def largestRectangleArea4(self, heights: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea3([2, 1, 5, 6, 2, 3]))
