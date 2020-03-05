# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and helper(a.left, b.right) and helper(a.right, b.left)
        return helper(root, root)
