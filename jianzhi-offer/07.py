# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        val = preorder[0]
        idx = inorder.index(val)

        left_pre = preorder[1:1+idx]
        right_pre = preorder[1+idx:]
        left_in = inorder[:idx]
        right_in = inorder[idx+1:]

        root = TreeNode(val)
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root
