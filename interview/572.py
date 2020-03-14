# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # 递归判断
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        if s == None:
            return False
        return self.is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        if r1 == None or r2 == None:
            return False
        return r1.val == r2.val and self.is_same(r1.left, r2.left) and self.is_same(r1.right, r2.right)

    # 序列化后判断

    def isSubtree2(self, s, t):
        def serialization(root, string):
            if not root:
                string += 'null,'
            else:
                string += ','+str(root.val)+','
                string = serialization(root.left, string)
                string = serialization(root.right, string)
            return string

        s1 = serialization(s, '')
        t1 = serialization(t, '')
        return t1 in s1
