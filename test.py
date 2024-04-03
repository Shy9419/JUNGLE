v, e = map(int, input().split())
graph = []
li = [0] * (v + 1)
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
graph.sort()

for i in range(1, v + 1):
    li[i] = i
    
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
    
for u in graph:
    cost, a, b = u
    if find(li, a) != find(li, b):
        union(li, a, b)
        result += cost
print(result)

    