# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

'''
输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
'''


class Solution(object):
    # greedy
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])

        end = intervals[0][1]
        # count 指不重叠子区间的最大个数
        count = 1

        for i in intervals:
            start = i[0]
            if start >= end:
                count += 1
                end = i[1]

        return len(intervals)-count
