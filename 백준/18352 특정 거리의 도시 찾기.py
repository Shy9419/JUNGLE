from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

