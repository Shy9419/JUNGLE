from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
# ??
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(x):
    answer = []
    #큐 구현을 위해 deque 라이브러리 사용.
    queue = deque([x])
    # 현재 노드를 방문처리
    visited[x] = True
    # ??
    distance[x] = 0
    while queue:
        # que에서 하나씩 원소를 뽑아서 출력
        v = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # ??
                distance[i] = distance[v] +1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
bfs(x)
