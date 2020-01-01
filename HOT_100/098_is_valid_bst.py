# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    '''
    乍一看，这是一个平凡的问题。只需要遍历整棵树，检查 node.right.val > node.val 和
    node.left.val < node.val 对每个结点是否成立

    But! 这种方法并不总是正确。不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点，如
          5
         / \
        1   7
           / \
          3   9
    这里的 3<5

    这意味着我们需要在遍历树的同时保留结点的上界与下界，在比较时不仅比较子结点的值，也要与上下界比较
    '''

    # 递归
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            if lower >= root.val or root.val >= upper:
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

        return helper(root)

    # 上述方法，使用栈转化为迭代

    def isValidBST2(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or upper <= val:
                return False

            stack.append((root.left, lower, val))
            stack.append((root.right, val, upper))

        return True

    # 利用中序遍历：我们需要保存整个遍历列表吗？
    # 不需要！ 维护一个变量即可
    def isValidBST3(self, root: TreeNode) -> bool:
        cur = root
        stack = []
        inorder = float('-inf')

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            val = cur.val
            if val <= inorder:
                return False
            inorder = val
            cur = cur.right

        return True
