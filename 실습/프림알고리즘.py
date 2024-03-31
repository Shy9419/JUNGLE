import sys
input = sys.stdin.readlines
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
edges = []
set_list = [0] * (V + 1)
result = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for i in range(1, V + 1):   # 노드번호
    set_list[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
        
for edge in edges:
    cost, a, b = edge
    if find(set_list, a) != find(set_list,b):
        union(set_list, a, b)
        result += cost
print(result)