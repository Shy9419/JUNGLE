import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if visited[u] == False:
            dfs(u)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)      # 'u'와 'v'를 연결하는 간선을 추가한다.
    graph[v].append(u)      # 무방향 그래프이므로 'v'와'u'와도 연결
    
dfs(1)
print(sum(visited) - 1)
