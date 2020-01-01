# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 递归
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def inorder(root, traversal_path):
            if root:
                inorder(root.left, traversal_path)
                traversal_path.append(root.val)
                inorder(root.right, traversal_path)

        traversal_path = []
        inorder(root, traversal_path)
        return traversal_path

    # 基于栈的遍历
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        cur = root
        stack = []
        traversal_path = []

        while cur or stack:
            while cur:
                # cur 入栈
                stack.append(cur)
                cur = cur.left
            # 树的最左出栈
            cur = stack.pop()
            traversal_path.append(cur.val)
            cur = cur.right

        return traversal_path
