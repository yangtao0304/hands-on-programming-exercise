from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(solution, cur_row):
            col = solution[cur_row].index('Q')
            for row in range(cur_row):
                cur_col = solution[row].index('Q')
                if cur_col == col or abs(cur_col-col) == cur_row-row:
                    return False
            return True

        def backtrack(solution, cur_row):
            if cur_row == n:
                output.append(solution[:])
                return

            for i in range(n):
                solution[cur_row] = '.'*i + 'Q' + '.'*(n-i-1)
                if check(solution, cur_row):
                    backtrack(solution, cur_row+1)
                solution[cur_row] = '.'*n

        output = []
        init_solution = ['.'*n for i in range(n)]
        backtrack(init_solution, 0)
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
