'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = INF to represent INF as you may assume that the distance to a gate is less than INF.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''

from collections import deque


class Solution(object):
    # BFS : 1. 借助queue， 首先把门的位置排入queue，开始循环
    #       2. 对于门位置的4个相邻点，判断其是否在矩阵范围内，并且值是否大于上一位置+1，满足则赋值为上一位置加1；并将次位置排入queue中
    #       3. queue中的元素遍历完，所有位置的值就被正确地更新了
    def walls_and_gates(self, rooms):
        queue = deque()
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        for i, row in enumerate(rooms):
            for j, item in enumerate(row):
                if item == 0:
                    queue.append((i, j))

        while len(queue) > 0:
            i, j = queue.popleft()
            for dx, dy in directions:
                i_next, j_next = i+dx, j+dy
                if (i_next < 0 or i_next >= len(rooms)
                    or j_next < 0 or j_next >= len(rooms[0])
                        or rooms[i_next][j_next] <= rooms[i][j]+1):
                    continue
                rooms[i_next][j_next] = rooms[i][j]+1
                queue.append((i_next, j_next))


if __name__ == "__main__":
    s = Solution()
    INF = 2147483647
    rooms = [[INF, -1, 0, INF],
             [INF, INF, INF, -1],
             [INF, -1, INF, -1],
             [0, -1, INF, INF]]
    s.walls_and_gates(rooms)
    print(rooms)

