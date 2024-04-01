import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# dfs 함수 
def dfs(v):
    visited[v] = True   # 값이 들어왔다는 건 방문했다는 거 트루로 바꿈
    for u in graph[v]:      # 현재 정점 'v' 와 연결된 모든 정점 'u'에 대해 반복해준다.
        if visited[u] == False:      # 정점 'u'를 방문하지 않았다면, 해당 정점에 대해 DFS를 재귀적으로 호출하여 연결된 모든 정점을 탐색한다.
            dfs(u)

# 입력값 받기 , 2차원 배열 그래프 만들기, 1차원 배열 방문여부 그래프 만들기
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 그래프 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)      # 'u'와 'v'를 연결하는 간선을 추가한다.
    graph[v].append(u)      # 무방향 그래프이므로 'v'와'u'와도 연결

# 연결 요소 개수 세기
count = 0
for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)
