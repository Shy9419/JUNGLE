# """
# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
# 상하죄우로 연결된 모든 노드로의 거리가 1로 동일하다
# 따라서 1,1 지점에서부터 VFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다.
# 예시로 다음과 같이 3x3 크기의 미로가 있다고 가정한다.

# 1. (1,1)위치에서 시작.
# 2. 상 하 좌 우로 탐색을 진행하면 바로 옆 노드인(1, 2).위치의 노드를 방문하게 되고 새롭게 방문하는 (1,2) 노드의 값을 2로 바꾸게 된다.
# 3. 마찬가지로 BFS를 계속 수행하면 결과적으로 다음과 같이 최단 경로의 값들이 1씩 증가하는 형태로 변경된다.
# 4. 마지막 값 출력
# """

# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(x,y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque() # 변수 queu에 deque()를 할당
#     queue.append((x,y))
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()  # q안에서 가장 왼쪽 첫 번째 요소를 제거하고 그 값을 변수 x 와 y에 각각 할당
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n -1][m -1]

# # n, m을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().strip())))
    
# # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# print(bfs(0,0))



import sys
from collections import deque ## 많은 상황에서 데큐가 좋습니다.
# double ended +  queue
# 양쪽 진입,삭제가능..
input = sys.stdin.readline
n,m = map(int,input().split())
lst = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for i in range(n):
    tmp = input().rstrip()
    lst.append(tmp)
board = [ [0] * (m) for _ in range(n) ] ## lst 는 임시로 받아온 것 입니다.
visited = [ [False] * m for _ in range(n) ]
for y in range(n): ## 행, y
    for x in range(m): ## 열, x
        if lst[y][x] == '0':
            board[y][x] = -1
        elif lst[y][x] == '1':
            board[y][x] = 0
## 0 은 갈 수 있는 길, -1 은 벽 입니다.
q = deque()
q.append([0,0])
while q:
    y,x = q.popleft() ## 큐에 왔으면 제일 먼저 할 것은, 큐에 있는 것 뺴줘야 합니다.
    visited[y][x] = True ##
    for i in range(4): # 0,1,2,3 -> 총 4개의 방향을 탐색하겠습니다.
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < n and 0 <= nx < m: #여기까지 왔으면, 맵 밖으로 벗어나는 일은 없습니다!
            if board[ny][nx] == 0 and visited[ny][nx] == False: # 갈 수 있는 길이며, 방문한 적이 없다면
                board[ny][nx] = board[y][x] + 1
                visited[ny][nx] = True
                q.append([ny,nx])
                # print("")
                # print("")
                # for r in range(n):
                #     for c in range(m):
                #         print(board[r][c],end ="\t")
                #     print("")
                # print("")