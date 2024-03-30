def find(self. value):
    for i in range(self.no):
        idx = (i + self.front) % self.capacity
        if self.que[idx] == value:
            return idx
    return -1

def recur(n):
    while n > 0:
        recur(n-1)
        print(n)
        n = n - 2