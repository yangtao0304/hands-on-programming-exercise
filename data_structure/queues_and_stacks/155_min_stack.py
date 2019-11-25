# 思想：“以空间换时间”，使用辅助栈是常见的做法
# ref: https://leetcode-cn.com/problems/min-stack/solution/shi-yong-fu-zhu-zhan-tong-bu-he-bu-tong-bu-python-/


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # data stack
        self.data = []
        # helper stack
        '''存最小值的栈具体操作如下：
        将第一个元素入栈
        新加入元素若大于栈顶元素，不操作
        新加入元素若小于等于栈顶元素，将新元素入栈
        出栈元素不等于栈顶元素，不操作
        出栈元素等于栈顶元素，将栈顶元素出栈'''
        self.helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            tmp = self.data.pop()
            if tmp == self.helper[-1]:
                self.helper.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]


# 使用一个变量储存最小值

class MinStack_2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # data stack
        self.data = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.min:
            self.data.append(self.min)
            self.min = x
        self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            tmp = self.data.pop()
            if tmp == self.min:
                self.min = self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
