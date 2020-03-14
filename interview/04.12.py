# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(r, s):
            if not r:
                return 0

            s = [i+r.val for i in s]+[r.val]
            return s.count(sum)+dfs(r.left, s)+dfs(r.right, s)
        return dfs(root, [])
