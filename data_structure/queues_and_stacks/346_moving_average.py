from collections import deque


class MovingAverage(object):
    def __init__(self, length):
        self.queue = deque()
        self.max_len = length

    def next(self, val):
        self.queue.append(val)
        if len(self.queue) > self.max_len:
            self.queue.popleft()
        return sum(self.queue) / len(self.queue)


if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))
