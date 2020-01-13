class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1])
        if not points:
            return 0
        count = 1
        end = points[0][1]
        for i in points:
            start = i[0]
            if start > end:
                count += 1
                end = i[1]
        return count
