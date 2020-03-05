# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret = []

        if not root:
            return ret

        def dfs(root, remain, path):
            path.append(root.val)
            if root.left == None and root.right == None and root.val == remain:
                ret.append(path[:])

            if root.left:
                dfs(root.left, remain-root.val, path)
                path.pop()
            if root.right:
                dfs(root.right, remain-root.val, path)
                path.pop()

        dfs(root, sum, [])
        return ret
