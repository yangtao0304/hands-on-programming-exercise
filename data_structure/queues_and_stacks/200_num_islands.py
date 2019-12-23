from collections import deque


class Solution(object):
    '''本题如何应用BFS？
    我们可以把每一个陆地点当作树根，用 BFS 搜索四周的陆地并沉没它，那么这一整块的陆地都被沉没了
    下次我们再遇到陆地点的时候就说明发现新大陆了'''

    def num_islands_bfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue = deque()
        visited = set()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 发现新大陆
                if grid[i][j] == '1':
                    queue.append((i, j))
                    visited.add((i, j))
                    num += 1

                # 旧大陆的消融
                while queue:
                    x, y = queue.popleft()
                    grid[x][y] = '0'
                    for dx, dy in directions:
                        x_next, y_next = x+dx, y+dy
                        if (0 <= x_next < len(grid) and 0 <= y_next < len(grid[0])
                                and grid[x_next][y_next] == '1'
                                and (x_next, y_next) not in visited):
                            queue.append((x_next, y_next))
                            visited.add((x_next, y_next))
        return num

    # dfs
    # refs: https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
    def num_islands_dfs(self, gird):
        pass

    # Union-find Sets
    def num_islands_ufs(self, gird):
        pass


# supplementary
# union-find sets
'''
并查集的应用场景一般是：动态连通性判断；例如，判断网络中的两台电脑是否连通；在程序中判断两个变量是否指向同一内存地址等

并查集逻辑上是森林，我们可以选出一个根节点作为代表，其他子节点指向根结点表示都在同一片森林
在这里，我们并不关心节点的子节点是谁，只关心父节点是谁

因此物理上可以简单用python的列表表示并查集，列表的下标表示节点，列表元素的值表示父节点
'''


class UnionFind(object):
    '''并查集的初始化，即用一种特殊的方式表示初始的每一个元素都不相交，等待后续的合并操作'''

    # def __init__(self, n):
    #     '''长度为n的并查集'''
    #     self.uf = [i for i in range(n+1)]
    #     self.sets_count = n

    def __init__(self, n):
        self.uf = [-1 for i in range(n+1)]  # 列表0的位置空出
        self.sets_count = n

    # 复杂度高 最坏O(n)
    # def find(self, p):
    #     '''查找p的根节点'''
    #     while self.uf[p] >= 0:
    #         p = self.uf[p]
    #     return p

    # 路径压缩
    def find(self, p):
        '''尾递归'''
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    # 尾递归 -> 改成循环方式
    # def find(self, p):
    #     '''查找p的根结点'''
    #     r = p
    #     while self.uf[p] > 0:
    #         p = self.uf[p]
    #     while r != p:
    #         self.uf[r], r = p, self.uf[r]  # 没看懂 23333
    #     return p

    # 把规模小的树往规模大的树上合并/树高小的往高度大的合并
    def union(self, p, q):
        '''连通p，q'''
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return
        elif self.uf[p_root] > self.uf[q_root]:  # 负数比较，左边规模更小
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]  # 规模相加
            self.uf[q_root] = p_root

        self.sets_count -= 1  # 连通后集合总数减1

    def is_connected(self, p, q):
        '''判断pq是否已经连通'''
        return self.find(p) == self.find(q)
