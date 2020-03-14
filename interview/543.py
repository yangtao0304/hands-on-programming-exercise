# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 对应root=None的情况，结果为0
        res = 1

        def depth(root):
            nonlocal res
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            res = max(res, l+r+1)
            return max(l, r)+1
        depth(root)
        return res-1
