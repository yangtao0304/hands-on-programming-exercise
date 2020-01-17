class Solution:
    # 贪心算法
    # 我们在n+1个时间内执行一轮
    # 若任务种类t小于n+1，就只选择t种任务
    # 该贪心策略的正确性：1.最多任务一定要优先执行； 2.能够保证两轮之间同一任务时间差>=n
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for task in tasks:
            count[ord(task)-ord('A')] += 1

        count.sort()
        time = 0

        while count[25] > 0:
            # n+1为一个周期
            i = 0
            while i <= n:
                if count[25] == 0:
                    break
                if i <= 25 and count[25-i] > 0:
                    count[25-i] -= 1
                time += 1
                i += 1
            count.sort()
        return time

    # 方法三待补充
    # ref: https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode/

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        pass
