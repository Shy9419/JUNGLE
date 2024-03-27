import sys


def get_input():
    return sys.stdin.readline().rstrip()


class MaxHeap:
    def __init__(self):
        self.tree = [None]
        self.size = 0

    def pop(self):
        if self.size < 1:
            return 0
        self.tree[1], self.tree[-1] = self.tree[-1], self.tree[1]
        root = self.tree.pop()
        self.size -= 1
        self.bubble_down(1)

        return root

    def push(self, value):
        self.size += 1
        cur_idx = self.size
        self.tree.append(value)
        self.bubble_up(cur_idx)

    def bubble_up(self, idx):
        parent = idx // 2
        while parent >= 1 and self.tree[parent] < self.tree[idx]:
            self.tree[parent], self.tree[idx] = self.tree[idx], self.tree[parent]
            idx = parent
            parent = parent // 2

    def bubble_down(self, idx):
        cur_idx = idx
        child_idx = cur_idx * 2  # left child
        while child_idx <= self.size:
            right_child_idx = child_idx + 1
            if right_child_idx <= self.size:
                child_idx = (
                    child_idx
                    if self.tree[child_idx] > self.tree[right_child_idx]
                    else right_child_idx
                )
            if self.tree[cur_idx] >= self.tree[child_idx]:
                break

            self.tree[cur_idx], self.tree[child_idx] = (
                self.tree[child_idx],
                self.tree[cur_idx],
            )
            cur_idx = child_idx
            child_idx *= 2


n = int(get_input())
max_heap = MaxHeap()
for i in range(n):
    user_input = int(get_input())
    if user_input == 0:
        print(max_heap.pop())
    else:
        max_heap.push(user_input)
