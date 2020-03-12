from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.helper = deque()

    def max_value(self) -> int:
        return self.helper[0] if self.helper else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.helper and self.helper[-1] < value:
            self.helper.pop()
        self.helper.append(value)

    def pop_front(self) -> int:
        if self.queue:
            tmp = self.queue.popleft()
            if tmp == self.helper[0]:
                self.helper.popleft()
            return tmp
        else:
            return -1


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
