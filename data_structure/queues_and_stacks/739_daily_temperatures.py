class Solution(object):
    '''
    规律: 要求出第i天对应的结果，只需要知道第i+1天对应的结果就可以：
    * - 若T[i] < T[i+1]，那么res[i]=1；
    * - 若T[i] > T[i+1]
    *   - res[i+1]=0，那么res[i]=0;
    *   - res[i+1]!=0，那就比较T[i]和T[i+1+res[i+1]]（即将第i天的温度与比第i+1天大的那天的温度进行比较）
    '''

    def daily_temperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0]*len(T)

        def get_res(i, j):
            if T[i] < T[j]:
                return j-i
            else:
                if res[j] == 0:
                    return 0
                else:
                    return get_res(i, j+res[j])

        for i in range(len(T)-2, -1, -1):
            res[i] = get_res(i, i+1)

        return res

    # ref: https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode/
    def daily_temperatures_official_1(self, T):
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            # Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans

    def daily_temperatures_official_2(self, T):
        pass


if __name__ == "__main__":
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.daily_temperatures(T))
