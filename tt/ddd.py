import sys


class MaxHeap:

    def __init__(self):
        self.li = [None]
        self.size = 0

    def push(self, value):
        self.li.append(value)
        self.size += 1
        index = self.size
        self.bubble_up(index)

    def get_max(self):
        if self.size == 0:
            return 0
        self.li[1], self.li[self.size] = self.li[self.size], self.li[1]
        max_val = self.li.pop()
        self.size -= 1
        self.bubble_down()
        return max_val

    def bubble_up(self, index):
        child_index = index
        parent_index = index // 2
        while child_index >= 2 and self.li[child_index] > self.li[parent_index]:
            self.li[child_index], self.li[parent_index] = (
                self.li[parent_index],
                self.li[child_index],
            )
            child_index = parent_index
            parent_index = child_index // 2

    def bubble_down(self):
        current_index = 1
        child_index = current_index * 2
        while child_index <= self.size:
            right_child_index = child_index + 1
            if right_child_index <= self.size:
                child_index = (
                    child_index
                    if self.li[child_index] > self.li[right_child_index]
                    else right_child_index
                )
            if self.li[current_index] >= self.li[child_index]:
                break
            if self.li[current_index] < self.li[child_index]:
                self.li[current_index], self.li[child_index] = (
                    self.li[child_index],
                    self.li[current_index],
                )
                current_index = child_index
                child_index *= 2  # 자기 자신 곱하기


n = int(sys.stdin.readline())
maxheap = MaxHeap()
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        sys.stdout.write(str(maxheap.get_max()) + "\n")
    else:
        maxheap.push(x)
