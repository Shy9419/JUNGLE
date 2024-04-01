V, E = map(int,input().split())
edges = []
li = [0] * (V - 1)
result = 0

for _ in range(E):      # 간선 리스트 만들고 정렬
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

for i in range(1, V + 1):   # 부모 리스트 초기화
    li[i] = i
    
def find (parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union (parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
        
for edge in edges:
    cost, a, b = edge
    if find(li, a) != find(li,b):
        union(li, a, b)
        result += cost
print(result)
        
    