# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(root):
            nonlocal ans
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            mid = root == p or root == q

            if left+mid+right == 2:
                ans = root

            return left or right or mid
        dfs(root)
        return ans
