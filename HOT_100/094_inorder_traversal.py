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


# 补充前序遍历
def pre_order(root):
    res = []
    cur = root
    stack = [cur]
    while stack:
        tmp = stack.pop()
        if tmp:
            res.append(tmp.val)
            # 先后后左
            stack.append(tmp.right)
            stack.append(tmp.left)


# 后序遍历
def post_order(root):
    res = []
    cur = root
    stack = [cur]
    while stack:
        tmp = stack.pop()
        if tmp:
            res.append(tmp.val)
            # 先左后右
            stack.append(tmp.left)
            stack.append(tmp.right)
    return reversed(res)
