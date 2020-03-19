# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]
        while queue:
            tmp = []
            t = len(queue)
            for _ in range(t):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        return res

    # official
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]
        level = 0
        while queue:
            res.append([])
            t = len(queue)
            for _ in range(t):
                cur = queue.pop(0)
                res[level].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return res

    # official 递归
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def helper(node, level):
            # 开始此level的遍历
            if len(res) == level:
                res.append([])

            # 添加当前node的val
            res[level].append(node.val)

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return res
