n = int(input())

for i in range(n - 1):
    a, b = map(int, input().split())

def dsf(v):
    visited[v] = True
    for u in graph[v]:
        if visited[u] == False:
            dfs[u]