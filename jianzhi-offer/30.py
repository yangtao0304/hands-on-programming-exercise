class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        if self.stack:
            tmp = self.stack.pop()
            if tmp == self.helper[-1]:
                self.helper.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def min(self) -> int:
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
