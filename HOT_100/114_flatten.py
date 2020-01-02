# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # in place
    # 题解：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            # 如果当前左子树为空，考虑下一个节点
            if not root.left:
                root = root.right

            else:
                # 找到左子树最右边的节点
                pre = root.left
                while pre.right:
                    pre = pre.right
                # 将原来右子树接到pre
                pre.right = root.right
                # 将左子树插入到右子树的地方
                root.right = root.left
                # 左子树置空
                root.left = None
                # 考虑下一个节点
                root = root.right
