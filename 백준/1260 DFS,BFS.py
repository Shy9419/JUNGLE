import sys
input = sys.stdin.readline

def dfs(idx):
    global visited      # 전역변수 visited(1차원 배열을 가져옴) v = 간선을 가져옴.
    visited[idx] = True     # 가져온 간선을 Ture로 바꿔줌 이미 실행됐으니까
    print(idx, end=' ')     # 현재 방문한 순서대로 출력을 해주는데 엔터가 아닌 띄어쓰기로 공백을 넣어줘
    for next in range(1, n +1):     # next라는 노드가 방문된적이 없고 방문 할 수 있다면 방문한다.
        if not visited[next] and graph[idx][next]:      # 만약에 다음 노드가 방문된적이 없고, 그리고 graph에서 인덱스의 넥스트가 있다면
            dfs(next)       # 재귀호출되어 다음 v값(간선)을 가져올테고 -> True로 바뀔테고 출력이 되고 for문을 통해 방문여부를 확인
    
def bfs():
    global q, visited
    while q:        # q의 요소가 남아있을 때 까지 빙글빙글 돈다.
        cur = q.pop(0)      # q의 가장 앞에 요소를 꺼내오고
        print(cur, end=' ')     # 프린트 한다 줄바꿈 없이 띄어쓰기형태로
        for next in range(1, n + 1):    # 방문한 곳이 있는지 확인
            if not visited[next] and graph[cur][next]:  # 만약에 다음 노드가 방문된적이 없고, 그리고 graph에서 cur에 넥스트가 있다면
                visited[next] = True        # 다음 노드를 방문처리한다.
                q.append(next)      # 그리고 다음 노드를 q에 추가한다.
    
n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
dfs(v)      # v노드부터 dfs를 실행해라
print()     # 줄바꿈

visited = [False] * (n + 1)
q = [v]
visited[v] = True
bfs()


