import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(u):
    for v in graph[u]:
        if visited[v] == False:
            visited[v] = u
            dfs(v)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
child = []


for _ in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

for x in range(2, n+1):
    print(visited[x])
    