class Solution(object):
    def find_diagonal_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        i = j = 0
        res = []
        for _ in range(row*col):
            res.append(matrix[i][j])
            if i == 0 and j % 2 == 0 and j < col-1:
                j += 1
            elif j == 0 and i % 2 == 1 and i < row-1:
                i += 1
            elif i == row-1 and (i+j) % 2 == 1:
                j += 1
            elif j == col - 1 and (i+j) % 2 == 0:
                i += 1
            elif (i+j) % 2 == 0:
                i -= 1
                j += 1
            elif (i+j) % 2 == 1:
                i += 1
                j -= 1
        return res

    def find_diagonal_order_2(self, matrix):
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        i = j = 0
        is_up = True
        res = []
        while True:
            res.append(matrix[i][j])
            if i == row-1 and j == col-1:
                return res

            if is_up:
                if i == 0 and j < col-1:
                    j += 1
                    is_up = False
                elif j == col-1:
                    i += 1
                    is_up = False
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < row-1:
                    i += 1
                    is_up = True
                elif i == row-1:
                    j += 1
                    is_up = True
                else:
                    i += 1
                    j -= 1
