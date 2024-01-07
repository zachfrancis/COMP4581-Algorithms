#!/usr/bin/env python3

from collections import deque

class MyStack:
    def __init__(self, t):
        assert isinstance(t, type)
        self.stack = []
        self.t = t

    def __str__(self):
        return str(self.stack)

    def pop(self):
        return self.stack.pop()

    def push(self, n):
        assert isinstance(n, self.t)
        self.stack.append(n)

    def top(self):
        return self.stack[-1]

    def empty(self):
        return False if self.stack else True

class MyQueue:
    def __init__(self, t):
        assert isinstance(t, type)
        self.queue = deque()
        self.t = t

    def __str__(self):
        return str(self.queue)

    def enqueue(self, n):
        assert isinstance(n, self.t)
        self.queue.append(n)

    def dequeue(self):
        return self.queue.popleft()

    def front(self):
        return self.queue[0]

    def empty(self):
        return False if self.queue else True

def main():
    # Testing code for stack
    s = MyStack(int)
    print(s.empty())
    s.push(5)
    s.push(8)
    print(s.pop())
    s.push(3)
    print(s.empty())
    print(s.top())
    print(s.pop())
    print(s.pop())
    #print(s.pop()) # should generate an error

    # Testing code for Queue
    q = MyQueue(int)
    print(q.empty())
    q.enqueue(5)
    q.enqueue(8)
    print(q.dequeue())
    q.enqueue(3)
    print(q.empty())
    print(q.front())
    print(q.dequeue())
    print(q.dequeue())
    #print(q.dequeue()) # should generate an error

if __name__ == "__main__":
    main()
