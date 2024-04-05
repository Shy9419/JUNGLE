from collections import deque

# 입력 값 받고
n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]
graph = []
# '-'입력받
for _ in range(m):
    a,b,c,d = map(str, input().strip())
    graph.append([a,b,c,d])
    
# 먼저 행을 기준으로 옆으로 가면서 값 비교하고 같으면 계속 진행
# 아니면 카운트를 올림
# 행이 끝나면 열을 바꿔서 진행
count = 0
def bfs(x,y):
    q = deque       # Queue를 만든다.
    q.append(x,y)   # 시작지점은 인큐한다.
    visited[x][y] = True    # 들어온 첫 번째 값을 방문처리한다.
    while q:    # 인접한 노드를 인큐 디큐 하고 방문처리하기 위해 반복한다.
        # 다음 값을 인큐
        if [nx][ny] == False and: # 만약에 다음 바닥 장식이 현재 장식과 같다면 또는 다음 바닥 장식을 아직 방문하지 않았다면.
            [nx][ny] = True # 바닥 장식을 방문처리
            continue    # 계속 탐색
        else:   # 만약 방문했던 곳이며, 그리고 바닥장식이 같지 않다면
            count += 1

    # for i in graph:
    #     if [i+1] == [i]:
    #         continue
    #     else:
    #         count += 1
    #     for j in i:
    #         if [j+1] == [j]:
    #             continue
    #         else:
    #             count += 1
print(count)
