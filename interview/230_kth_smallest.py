# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 中序遍历
    # 如果求第k大，则改变访问顺序即可
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            cur = root
            stack = []
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left

                cur = stack.pop()
                yield cur.val
                cur = cur.right

        gen = inorder(root)
        for i in range(k):
            res = next(gen)

        return res

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        i = 0
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            i += 1
            if i == k:
                return cur.val
            cur = cur.right

        gen = inorder(root)
        for i in range(k):
            res = next(gen)

        return res
