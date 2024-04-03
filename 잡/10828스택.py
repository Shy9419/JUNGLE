# 파이썬은 리스트가 모든 기능을 가지고 있다.
# push -> append 자료를 넣는 작업
# pop -> pop    자료를 꺼내는 작업
# size -> len   스택에 크기
# empty -> if stack:    원소가 있으면 트루로 없으면 펄스로
# top -> stack[-1]  스택에 마지막 원소를 가져옴 리스트 인덱스를 가져오는 방법으로 해결

import sys


class Stack:

    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def push(self, value):
        if self.ptr < self.capacity:
            self.stk[self.ptr] = value
            self.ptr += 1

    def pop(self):
        if self.is_empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr <= 0

    def empty(self):
        if self.is_empty():
            return 1
        else:
            return 0

    def peek(self):
        if self.is_empty():
            return -1
        else:
            return self.stk[self.ptr - 1]


n = int(sys.stdin.readline())

stk = Stack(n)

for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == "push":
        stk.push(s[1])
    elif s[0] == "pop":
        print(stk.pop())
    elif s[0] == "size":
        print(stk.__len__())
    elif s[0] == "empty":
        print(stk.empty())
    elif s[0] == "top":
        print(stk.peek())
