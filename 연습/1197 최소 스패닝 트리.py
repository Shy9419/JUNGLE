import sys
from collections import deque


INF = sys.maxsize


v, e = map(int, input().split())
graph = []
li = [0] * (v+1)
result = 0


for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()

for i in range(1, v+1):
    li[i] = i

def find(parent, x):
    if parent[x] != x :
        parent[x] = find(parent, x)
        return parent[x]
    
def union(parent, x, y):
    x = find(parent,x)
    y = find(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    

for u in graph:
    c, a, b = u
    if find(li, a) != find(li, b):
        union(li, a, b)
        result += c
print(result)
    

    
    
    