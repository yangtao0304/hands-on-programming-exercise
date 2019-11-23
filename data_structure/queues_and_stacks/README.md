## 1.1 概览
在数组中，我们可以通过索引访问随机元素。 但是，在某些情况下，我们可能想要限制处理顺序。
我们将介绍两种不同的处理顺序，先入先出和后入先出
以及两个相应的线性数据结构，队列和栈

## 2.1 队列：先入先出的数据结构
```
#include <iostream>

class MyQueue {
    private:
        // store elements
        vector<int> data;       
        // a pointer to indicate the start position
        int p_start;            
    public:
        MyQueue() {p_start = 0;}
        /** Insert an element into the queue. Return true if the operation is successful. */
        bool enQueue(int x) {
            data.push_back(x);
            return true;
        }
        /** Delete an element from the queue. Return true if the operation is successful. */
        bool deQueue() {
            if (isEmpty()) {
                return false;
            }
            p_start++;
            return true;
        };
        /** Get the front item from the queue. */
        int Front() {
            return data[p_start];
        };
        /** Checks whether the queue is empty or not. */
        bool isEmpty()  {
            return p_start >= data.size();
        }
};

int main() {
    MyQueue q;
    q.enQueue(5);
    q.enQueue(3);
    if (!q.isEmpty()) {
        cout << q.Front() << endl;
    }
    q.deQueue();
    if (!q.isEmpty()) {
        cout << q.Front() << endl;
    }
    q.deQueue();
    if (!q.isEmpty()) {
        cout << q.Front() << endl;
    }
}
```
## 2.2 循环队列
此前，我们提供了一种简单但低效的队列实现

更有效的方法是使用循环队列
具体来说，我们可以使用固定大小的数组和两个指针来指示起始位置和结束位置。 目的是重用我们之前提到的被浪费的存储

## 2.3 循环队列实现
在循环队列中，我们使用一个数组和两个指针（head 和 tail）
head 表示队列的起始位置，tail 表示队列的结束位置
```
class MyCircularQueue {
private:
    vector<int> data;
    int head;
    int tail;
    int size;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        data.resize(k);
        head = -1;
        tail = -1;
        size = k;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        if (isEmpty()) {
            head = 0;
        }
        tail = (tail + 1) % size;
        data[tail] = value;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        if (head == tail) {
            head = -1;
            tail = -1;
            return true;
        }
        head = (head + 1) % size;
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return data[head];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[tail];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return head == -1;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return ((tail + 1) % size) == head;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * bool param_1 = obj.enQueue(value);
 * bool param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * bool param_5 = obj.isEmpty();
 * bool param_6 = obj.isFull();
 */
 ```

 ## 2.4 队列-用法
```
#include <iostream>

int main() {
    // 1. Initialize a queue.
    queue<int> q;
    // 2. Push new element.
    q.push(5);
    q.push(13);
    q.push(8);
    q.push(6);
    // 3. Check if queue is empty.
    if (q.empty()) {
        cout << "Queue is empty!" << endl;
        return 0;
    }
    // 4. Pop an element.
    q.pop();
    // 5. Get the first element.
    cout << "The first element is: " << q.front() << endl;
    // 6. Get the last element.
    cout << "The last element is: " << q.back() << endl;
    // 7. Get the size of the queue.
    cout << "The size is: " << q.size() << endl;
}
```

## 3.1 队列和BFS
广度优先搜索（BFS）的一个常见应用是找出从根结点到目标结点的最短路径

* 如果在第 k 轮中将结点 X 添加到队列中，则根结点与 X 之间的最短路径的长度恰好是 k。也就是说，第一次找到目标结点时，你已经处于最短路径中

## 3.2 广度优先搜索-模版
使用 BFS 的两个主要方案：遍历或找出最短路径

* 模版I
```
/**
 * Return the length of the shortest path between root and target node.
 */
 int BFS(Node root, Node target)
 {
     Queue<Node> queue;
     int step = 0;
     // initialize
     add root to queue;
     // BFS
     while (queue is not empty){
         step = step + 1;
         // iterate the nodes which are already in the queue
         int size = queue.size();
         for (int i = 0; i < size; ++i){
             Node cur = the first node in queue;
             return step if cur is target;
             for (Node next : the neighbors of cur){
                 add next to queue;
             }
             remove the first node from queue;
         }
     }
     return -1; //there is no path from root to target
 }
 ```
1. 如代码所示，在每一轮中，队列中的结点是***等待处理的结点***
2. 在每个更外一层的 while 循环之后，我们距离根结点更远一步。变量 ***step*** 指示从根结点到我们正在访问的当前结点的距离

* 模版II
有时，确保我们永远***不会访问一个结点两次***很重要。否则，我们可能陷入无限循环。如果是这样，我们可以在上面的代码中添加一个哈希集来解决这个问题
```
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> used;  // store all the used nodes
    int step = 0;  // number of steps needed from root to current node
    // initialize
    add root to queue;
    add root to used;
    // BFS
    while (queue is not empty){
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i){
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next: the neighbors of cur){
                if (next is not in used){
                    add next to queue;
                    add next to used;
                }
            }
            remove the first node from queue;
        }
    }
    return -1;  // there is no path from root to target
}
```
有两种情况你不需要使用哈希集：

1. 你完全确定没有循环，例如，在树遍历中
2. 你确实希望多次将结点添加到队列中