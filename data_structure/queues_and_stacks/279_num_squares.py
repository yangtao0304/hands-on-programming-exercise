from collections import deque


class Solution(object):
    # bfs
    def num_squares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = deque([(n, 0)])
        visited = set([n])

        while queue:
            num, step = queue.popleft()
            remains = [num-n*n for n in range(1, int(num**0.5)+1)]
            for i in remains:
                if i == 0:
                    return step+1
                if i not in visited:
                    queue.append((i, step+1))
                    visited.add(i)

    # dp
    # ref: https://leetcode-cn.com/problems/perfect-squares/solution/hua-jie-suan-fa-279-wan-quan-ping-fang-shu-by-guan/
    '''
    思路：动态规划
    首先初始化长度为n+1的数组dp，每个位置都为0
    如果n为0，则结果为0
    对数组进行遍历，下标为i，每次都将当前数字先更新为最大的结果，即dp[i]=i，比如i=4，最坏结果为4=1+1+1+1即为4个数字
    动态转移方程为：dp[i] = MIN(dp[i], dp[i - j * j] + 1)，i表示当前数字，j*j表示平方数
    时间复杂度：O(n*sqrt(n))，sqrt为平方根
    '''

    def num_squares_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.num_squares(3))
