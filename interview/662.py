# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # bfs
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = [(root, 0, 0)]
        cur_depth = 0
        ans = 0
        left = 0
        for node, depth, position in queue:
            if node:
                queue.append((node.left, depth+1, 2*position))
                queue.append((node.right, depth+1, 2*position+1))
                if depth != cur_depth:
                    cur_depth = depth
                    left = position
                ans = max(position-left+1, ans)
        return ans

    # dfs
    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        left = dict()
        ans = 0

        def dfs(root, depth=0, pos=0):
            nonlocal ans
            if root:
                if depth not in left:
                    left[depth] = pos
                ans = max(ans, pos-left[depth]+1)
                dfs(root.left, depth+1, pos*2)
                dfs(root.right, depth+1, pos*2+1)
        dfs(root)
        return ans
