from collections import deque


class Solution(object):
    '''广度优先遍历
    我们可以将0000-9999这10000状态看成图上的10000个节点
    两个节点之间存在一条边，当且仅当这两个节点对应的状态只有1位不同，且不同的1位相差1（包括0和9之间）
    并且这两个节点均不在deadends中
    那么最终的答案即为0000-target的最短路径

    我们用广度优先搜索来找到最短路径，从0000开始搜索
    对于每一个状态，它可以扩展到最多8个状态
    将这些状态中没有搜索过并且不再deadends中的状态全部加入到队列，并继续进行搜索
    注意：0000本身有可能也在deadends中'''

    # 超时
    def open_lock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        queue = deque()
        visited = set()
        # 加set后就过了 2333
        dead = set(deadends)

        if '0000' in dead:
            return -1

        queue.append('0000')
        visited.add('0000')
        step = -1

        while len(queue) != 0:
            step += 1
            size = len(queue)
            for i in range(size):
                cur_state = queue.popleft()
                if cur_state == target:
                    return step
                for next_state in neighbors(cur_state):
                    if next_state not in dead and next_state not in visited:
                        queue.append(next_state)
                        visited.add(next_state)

        return -1

    def openLock_official(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
