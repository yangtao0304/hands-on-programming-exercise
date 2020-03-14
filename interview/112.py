# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, sum-root.val)]
        while stack:
            node, val = stack.pop()
            if node.left == None and node.right == None and val == 0:
                return True
            if node.left:
                stack.append((node.left, val-node.left.val))
            if node.right:
                stack.append((node.right, val-node.right.val))
        return False
