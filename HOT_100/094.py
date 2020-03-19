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
    if not root:
        return res

    stack = [root]
    while stack:
        tmp = stack.pop()
        res.append(tmp.val)
        # 先右后左
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)


# 后序遍历
def post_order(root):
    res = []
    stack = [root]
    while stack:
        tmp = stack.pop()
        if tmp:
            res.append(tmp.val)
            # 先左后右
            stack.append(tmp.left)
            stack.append(tmp.right)
    return reversed(res)


def post_order(root):
    # use 2 stack
    if not root:
        return []
    stack1 = [root]
    stack2 = []

    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)

    res = []
    while stack2:
        cur = stack2.pop()
        res.append(cur.val)
    return res

# 二叉树的遍历的时间复杂度都是O(n)
# 空间复杂度都是O(L), L是二叉树的层数


# 二叉树的层次遍历
def level_order(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        n = len(queue)
        tmp = []
        for i in range(n):
            cur = queue.pop(0)
            tmp.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res.append(tmp)
    return res


def level_order2(root):
    if not root:
        return []

    cur_level = [root]
    res = []
    while cur_level:
        tmp = []
        next_level = []
        for i in cur_level:
            tmp.append(i.val)
            if i.left:
                next_level.append(i.left)
            if i.right:
                next_level.append(i.right)
        res.append(tmp)
        cur_level = next_level
    return res


# 二叉树的锯齿形层次遍历
# 使用两个栈
def zigzag_level_order(root):
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    res = []

    while stack1 or stack2:
        tmp = []
        if stack1:
            while stack1:
                cur = stack1.pop()
                tmp.append(cur.val)
                if cur.left:
                    stack2.append(cur.left)
                if cur.right:
                    stack2.append(cur.right)
        else:
            while stack2:
                cur = stack2.pop()
                tmp.append(cur.val)
                if cur.right:
                    stack1.append(cur.right)
                if cur.left:
                    stack1.append(cur.left)
        res.append(tmp)
    return res

# 二叉树的序列化和反序列化
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def recursive(root, string):
            if not root:
                string += 'null,'
            else:
                string += str(root.val)+','
                string = recursive(root.left, string)
                string = recursive(root.right, string)
            return string

        return recursive(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def recursive(data):
            if data[0] == 'null':
                data.pop(0)
                return None
            root = TreeNode(int(data[0]))
            data.pop(0)
            root.left = recursive(data)
            root.right = recursive(data)
            return root
            
        data = data.split(',')
        return recursive(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
