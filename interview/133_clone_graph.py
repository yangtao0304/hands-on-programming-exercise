"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}

        def dfs(node):
            if not node:
                return
            if node in d:
                return d[node]
            cp_node = Node(node.val, [])
            for i in node.neighbors:
                cp_node.neighbors.append(dfs(i))
            return cp_node

        return dfs(node)
