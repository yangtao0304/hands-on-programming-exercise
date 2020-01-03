'''
LRU: least recently used

在O(1)复杂度，完成put和get操作
'''

# 有序字典
# 哈希表+双向链表
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 在双向链表实现中，这里使用一个伪头部和伪尾部标记界限，这样在更新的时候就不需要检查是否是 null 节点

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # head, tail
        self.head = ListNode()
        self.tail = ListNode()
        # initialize
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key):
        # 移除key所指的节点
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 将node插入tail前
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_tail(key)

        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key)
            self.hashmap[key].value = value
        else:
            if len(self.hashmap) == self.capacity:
                # 注意不要忘记pop掉hashmap的对应值
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
