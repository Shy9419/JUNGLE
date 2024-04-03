from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 입력 처리
n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수

# 그래프 초기화
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())
    
def bfs(u):
    # 간선의 가중치를 비교하기 위해서 무한대로 초기화한 리스트 만듦
    distance = [INF] * (n+1)
    distance[u] = 0
    # 큐에 내용을 넣는다.
    q = deque([(u, 0)])
    # 큐에 내용이 다 빠질 때 까지 반복한다.
    while q:
        u, dist = q.popleft()   # 큐에서 팝한다.
        if dist > distance[u]:  # 간선의 가중치를 비교 : 만약 팝된 가중치가 크다면 다른 가중치
            continue
        # 
        for v, v_dist in graph[u]:
            cost = dist + v_dist    # 
            if cost < distance[v]:
                distance[v] = cost
                q.append((v, cost))
    return distance

# BFS로 출발 도시에서의 최소 거리를 구함
distances = bfs(start)

# 도착 도시까지의 최소 비용 출력
print(distances[end])
                



    