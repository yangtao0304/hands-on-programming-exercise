# coding: utf-8


class Solution(object):
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # recursive
        if not matrix:
            return []
        ret = []
        ret.extend(matrix[0])
        matrix_left = [reversed(i) for i in matrix[1:]]
        if not matrix_left:
            return ret
        r = self.spiral_order([i for i in zip(*matrix_left)])
        ret.extend(r)
        return ret

    def spiral_order_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res

    def spiral_order_official_1(self, matrix):
        # 绘制螺旋轨迹路径，我们发现当路径超出界限或者进入之前访问过的单元格时，会顺时针旋转方向

        # 思路：假设数组有 R 行 C 列，seen[r][c] 表示第 r 行第 c 列的单元格之前已经被访问过了
        # 当前所在位置为 (r, c)，前进方向是 di。我们希望访问所有 R x C 个单元格
        # 当我们遍历整个矩阵，下一步候选移动位置是 (cr, cc)
        # 如果这个候选位置在矩阵范围内并且没有被访问过，那么它将会变成下一步移动的位置
        # 否则，我们将前进方向顺时针旋转之后再计算下一步的移动位置
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        seen = [[False for _ in range(col)] for _ in range(row)]
        direction = {'right':[0,1], 'down':[1,0], 'left':[0,-1], 'up':[-1,0]}
        keys = ['right', 'down', 'left', 'up']
        
        res = []
        r = 0
        c = -1

        di = 0
        count = 0
        while True:
            r += direction[keys[di]][0]
            c += direction[keys[di]][1]
            if r>=0 and r<row and c>=0 and c<col and seen[r][c]==False:
                res.append(matrix[r][c])
                seen[r][c]=True
                count += 1
            else:
                r -= direction[keys[di]][0]
                c -= direction[keys[di]][1]
                di += 1
                di %= 4
            if count == row*col:
                break

        return res
                
    def spiral_order_official(self, matrix):
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.spiral_order_official_1(matrix))
