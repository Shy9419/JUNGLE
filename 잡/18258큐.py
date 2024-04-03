import sys


class Que:
    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def enque(self, value):
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        x = self.que[self.front]
        if x is None: return -1
        self.que[self.front] = None
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
        


    def size(self):
        return self.no
    # def count(self, value):
    #     c = 0
    #     for i in range(self.no):
    #         idx = (i + self.front) % self.capacity
    #         if self.que[idx] == value:
    #             c += 1
    #     return c

    def is_empty(self):
        return self.no <= 0

    def empty(self):
        if self.is_empty():
            return 1
        else:
            return 0

    def fornt(self):
        if self.is_empty():
            return -1
        else:
            return self.que[self.front]

    def back(self):
        if self.is_empty():
            return -1
        else:
            last_index = (self.rear - 1 + self.capacity) % self.capacity
            return self.que[last_index]


n = int(sys.stdin.readline())
print = sys.stdout.write

que = Que(n)

for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == "push":
        que.enque(s[1])
    elif s[0] == "pop":
        print(str(que.deque())+'\n')
    elif s[0] == "front":
        print(str(que.fornt())+'\n')
    elif s[0] == "back":
        print(str(que.back())+'\n')
    elif s[0] == "size":
        print(str(que.size())+'\n')
    elif s[0] == "empty":
        print(str(que.empty())+'\n')
