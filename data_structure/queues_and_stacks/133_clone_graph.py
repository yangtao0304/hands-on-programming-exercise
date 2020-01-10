# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# 给定无向连通图中一个节点的引用，返回该图的深拷贝


class Solution:
    # DFS recursive
    def cloneGraph(self, node: Node) -> Node:
        def dfs(node):
            if node in d:
                return d[node]
            clone = Node(node.val, [])
            d[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        if not node:
            return

        d = {}
        return dfs(node)

    # DFS iterative
    def cloneGraph2(self, node: Node) -> Node:
        if not node:
            return
        node_copy = Node(node.val, [])
        d = {node: node_copy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in d:
                    neighbor_copy = Node(neighbor.val, [])
                    d[neighbor] = neighbor_copy
                    d[node].neighbors.append(neighbor_copy)
                    stack.append(neighbor)
                else:
                    d[node].neighbors.append(d[neighbor])

        return node_copy

    # BFS iterative

    def cloneGraph3(self, node: Node) -> Node:
        if not node:
            return
        queue = [node]
        node_copy = Node(node.val, [])
        d = {node: node_copy}
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in d:
                    neighbor_copy = Node(neighbor.val, [])
                    d[neighbor] = neighbor_copy
                    d[node].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
                d[node].neighbors.append(d[neighbor])

        return node_copy
