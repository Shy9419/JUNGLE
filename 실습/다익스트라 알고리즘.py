"""
다이슥트라 알고리즘은 정렬 이후 
그리드 알고리즘.
컴퓨터는 하나씩 밖에 계산하지 못한다.

첫 노드에 가선치를 입력받음
그중 가장 작은 것을 비교해서 선택
현재까지 알고 있던 최단 경로를 계속해서 갱신

1. 출발점을 정의
2. 출발점을 기준으로 각 노드의 최소비용 저장
3. 방문하지 않은 노드중에 가장 작은 비용 노드 선택
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 계산
5. 위 과장에서 3~4를 반복

첫 노드를 선택하고 배열을 갱신(저장), 연결이 되지 않은 노드들은 무한으로 처리

"""
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
for i in range(E):
    u,v,w = map(int, input().split())
    edge[u].append([w,v])    #간선 인접리스트에 저장 : 1번 노드에 간선들을 리스트형태로 저장 ex) 1 = [(2,2)] 2번 노드로 2만큼의 비용으로 간다. 비용은 앞에

# 시작점 초기화
dist[K] = 0
heap = [[0,K]]

while heap:
    ew, ev = heapq.heappop(heap)    # ew = 지금 간선 값, ev = 지금 노드위치
    if dist[ev] != ew: continue     # 만약 두 값이 다르다면 이미 최단 거리가 업데이트 되었으므로 해당 노드를 다시 방문할 필요x
    for nw, nv in edge[ev]:     # 인접리스트에 값을 가지고 for문
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])        # heap 리스트에 dist[nv], nv를 추가하는 거.
            
for i in range(1, V + 1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])




# import sys
# input = sys.stdin.readline
# from queue import PriorityQueue

# V, E = map(int, input().split())
# K = int(input())
# distance = [sys.maxsize] * (V + 1)
# visited = [False] * (V + 1)
# mylist = [[] for _ in range(V + 1)]
# q = PriorityQueue()

# for _ in range(E):      # 엣지에 개수만큼 반복
#     u, v, w = map(int, input().split())
#     mylist[u].append((v,w))     #도착 노드와 가중치 인접리스트에
    
# q.put((0,K))        # 0을 먼저 쓰는 이유는 우선순위큐에서 앞에 거를 기준으로 자동정렬이된다. 따라서 현재 노드의 거리배열 리스트 값을 넣음.
# distance[K] = 0

# while q.qsize() > 0:
#     current = q.get()       # 현재 노드
#     c_v = current[1]
#     if visited[c_v]:
#         continue
#     visited[c_v] = True
#     for temp in mylist[c_v]:
#         next = temp[0]
#         value = temp[1]
#         if distance[next] > distance[c_v] + value:
#             distance[next] = distance[c_v] + value
#             q.put((distance[next], next))
            
# for i in range(1, V+1):
#     if visited[i]:
#         print(distance[i])
#     else:
#         print("INF")



import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)
INF = float('inf')
V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range (V + 1)]
for i in range (1, E + 1) :
    a, b, cost = map(int, input().split())
    edge[a].append((cost, b))
edge_cost = [INF for _ in range (V + 1)]

def dijkstra (x) :
    edge_cost[x] = 0
    queue = [[0, x]]
    while queue :
        cost, node = heapq.heappop(queue)
        if cost > edge_cost[node] :
            continue
        for c, d in edge[node] :
            if edge_cost[d] > edge_cost[node] + c :
                edge_cost[d] = edge_cost[node] + c
                heapq.heappush(queue, [edge_cost[d], d])
    print (edge_cost[1:])
print (edge)
dijkstra(K)


n, m = map(int,input().split())
k = int(input())
INF = sys.maxsize

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작 노드는 0으로 초기화
    visited[start] = True
    
    for i in graph[start]:
        now = get_smallest_node()   # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선ㅌ개
        visited[now] = True     # 방문 처리
        
        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
                
dijkstra(k)
print(distance)