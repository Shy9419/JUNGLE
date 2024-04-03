from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
ans = [0] * (n + 1)
ans[n] = 1      # 왜 1?
for _ in range(m):
    x, y, k = map(int,(input().split()))
    graph[x].append((y,k))
    indegree[y] += 1
    

queue = deque([n])
origin = [i for i in range(1, n + 1) if not graph[i]]

while queue:
    current = queue.popleft()
    for nxt,cnt in graph[current]:
        indegree[nxt] -= 1
        ans[nxt] += cnt*ans[current]
        if not indegree[nxt]:
            queue.append(nxt)

for i in origin:
    print(i, ans[i])