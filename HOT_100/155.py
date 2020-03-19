class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if x <= self.min:
            self.data.append(self.min)
            self.min = x
        self.data.append(x)

    def pop(self) -> None:
        if self.data:
            tmp = self.data.pop()
            if tmp == self.min:
                self.min = self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        return self.min


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or self.helper[-1] >= x:
            self.helper.append(x)

    def pop(self) -> None:
        if self.data:
            tmp = self.data.pop()
            if tmp == self.helper[-1]:
                self.helper.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
