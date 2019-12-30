'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        n = len(intervals)
        res = []
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            while i < n-1 and intervals[i+1][0] <= right:
                right = max(right, intervals[i+1][1])
                i += 1
            res.append([left, right])
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
