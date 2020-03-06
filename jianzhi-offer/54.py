# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            cur = root
            stack = []
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.right
                cur = stack.pop()
                yield cur.val
                cur = cur.left

        for idx, i in enumerate(inorder(root)):
            if idx == k-1:
                return i
