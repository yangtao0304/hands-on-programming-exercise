# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(root, sum, path):
            if root:
                if root.left == None and root.right == None and sum-root.val == 0:
                    res.append(path+[root.val])
                dfs(root.left, sum-root.val, path+[root.val])
                dfs(root.right, sum-root.val, path+[root.val])
        dfs(root, sum, [])
        return res
