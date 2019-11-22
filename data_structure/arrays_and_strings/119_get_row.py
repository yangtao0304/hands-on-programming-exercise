class Solution(object):
    # O(k)复杂度

    # 方法1: 杨辉三角的第 k 行等价于，二项式 (x + y)^k 的系数

    # 方法2: dp
    '''
    模拟法（动态规划）

    1.特判，若k==0，返回[1]
    2.初始化dp=[1,1]，表示第二行
    3.遍历区间[3,k+2)，表示从第三行开始遍历：
        初始化cur=[1,0,...,0,1]，长度为当前行数
        从cur第二个元素到倒数第二个元素，利用动态规划：cur[j]=dp[j-1]+dp[j]
        将dp更新为cur
    4.返回dp
    复杂度分析
    时间复杂度：O(k^{2})，等差数列求和
    空间复杂度：O(k)
    '''

    def get_row(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        dp = [1, 1]
        for line in range(3, rowIndex+2):
            cur = [1]+[0]*(line-2)+[1]
            for idx in range(1, line-1):
                cur[idx] = dp[idx-1]+dp[idx]
            dp = cur
        return dp

    def get_row_2(self, rowIndex):
        # j行的数据, 应该由j - 1行的数据计算出来.
        # 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
        # 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
        r = [1]
        for i in range(1, rowIndex + 1):
            r = r + [0]
            r_r = [0] + r
            for i in range(len(r)):
                r[i] = r[i]+r_r[i]
        return r
