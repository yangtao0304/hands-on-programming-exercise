class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.top_num = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        self.top_num = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp = None
        while self.queue1:
            tmp = self.queue1.pop(0)
            if len(self.queue1) == 1:
                self.top_num = tmp
            if len(self.queue1) != 0:
                self.queue2.append(tmp)

        self.queue1, self.queue2 = self.queue2, self.queue1
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_num

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
