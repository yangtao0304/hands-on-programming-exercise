# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # recursive
    # 与求树的最大高度类似
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def helper(root):
            nonlocal max_sum
            if not root:
                return 0

            # left,right非负，代表左右子树的最大值
            left = helper(root.left)
            right = helper(root.right)

            # 可能不过根节点，每个阶段都比较一次
            max_sum = max(max_sum, left+right+root.val)

            # 排除掉负值
            return max(0, max(left, right)+root.val)

        helper(root)
        return max_sum
