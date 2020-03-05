# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def is_subtree(A, B):
            if not B:
                return True
            if not A:
                return False
            return A.val == B.val and is_subtree(A.left, B.left) and is_subtree(A.right, B.right)

        if not B:
            return False
        if not A:
            return False

        return is_subtree(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
