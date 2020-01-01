# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        val = preorder[0]
        root = TreeNode(val)

        in_index = inorder.index(val)
        left_inorder = inorder[:in_index]
        right_inorder = inorder[in_index+1:]

        # pre_index = len(left_inorder)
        # left_preorder = preorder[1:pre_index+1]
        # right_preorder = preorder[pre_index+1:]
        left_preorder = preorder[1:in_index+1]
        right_preorder = preorder[in_index+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
