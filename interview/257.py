# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def dfs(root, path):
            if root:
                path += str(root.val)
                if root.left == None and root.right == None:
                    res.append(path)
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)
        dfs(root, '')
        return res
