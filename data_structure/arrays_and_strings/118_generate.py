class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                tmp = res[-1]
                res_tmp = [1]
                for i in range(len(tmp)-1):
                    res_tmp.append(tmp[i]+tmp[i+1])
                res_tmp.append(1)
                res.append(res_tmp)
        return res

    def generate_2(self, numRows):
        res = []
        for i in range(numRows):
            row = (i+1)*[1]
            if i >= 2:
                for idx in range(1, i):
                    row[idx] = pre[idx-1]+pre[idx]
            res += [row]
            pre = row
        return res

    def generate_official(self, numRows):
        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # dynamic programming
            # dp[i][j]=dp[i−1][j−1]+dp[i−1][j]
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle

    def generate_3(self, numRows):
        # initialize dp 
        dp = [[0]*n for n in range(1, numRows+1)]
        for i in range(numRows):
            dp[i][0] = dp[i][-1] = 1
        # traverse dp
        for i in range(0, numRows):
            for j in range(i+1):
                if dp[i][j]==0:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        
        return dp