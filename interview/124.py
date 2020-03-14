# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def dfs(root):
            nonlocal max_sum

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            max_sum = max(max_sum, left+right+root.val)

            return max(0, max(left, right)+root.val)

        dfs(root)
        return max_sum
