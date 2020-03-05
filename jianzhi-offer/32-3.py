# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # two stacks
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        ret = []
        time = 1

        while stack:
            tmp = []
            stack2 = []
            n = len(stack)
            for _ in range(n):
                node = stack.pop()
                tmp.append(node.val)
                if time % 2 == 1:
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
                else:
                    if node.right:
                        stack2.append(node.right)
                    if node.left:
                        stack2.append(node.left)
            time += 1
            stack = stack2
            ret.append(tmp)
        return ret
