# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 递归
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS迭代
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            t = len(queue)
            for i in range(t):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth

    # DFS迭代
    def maxDepth3(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        stack = [(root, 1)]
        while stack:
            cur_node, cur_depth = stack.pop()
            depth = max(depth, cur_depth)
            if cur_node.left:
                stack.append((cur_node.left, cur_depth+1))
            if cur_node.right:
                stack.append((cur_node.right, cur_depth+1))
        return depth
