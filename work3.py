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
        