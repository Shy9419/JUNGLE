import sys
from collections import deque


n, m = map(int, input().split())
li = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for i in range(n):
    tmp = input().rstrip()
    li.append(tmp)
board = [[0] * (m) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if li[y][x] == '0':
            board[y][x] = -1
        elif li[y][x] == '1':
            board[y][x] = 0
            
q = deque()
q.append([0,0])
while q:
    y, x = q.popleft()
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 0 and visited[ny][nx] == False:
                board[ny][nx] = board[y][x] + 1
                visited[ny][nx] = True
                q.append([ny,nx])