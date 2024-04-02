"""
BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
상하죄우로 연결된 모든 노드로의 거리가 1로 동일하다
따라서 1,1 지점에서부터 VFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다.
예시로 다음과 같이 3x3 크기의 미로가 있다고 가정한다.

1. (1,1)위치에서 시작.
2. 상 하 좌 우로 탐색을 진행하면 바로 옆 노드인(1, 2).위치의 노드를 방문하게 되고 새롭게 방문하는 (1,2) 노드의 값을 2로 바꾸게 된다.
3. 마찬가지로 BFS를 계속 수행하면 결과적으로 다음과 같이 최단 경로의 값들이 1씩 증가하는 형태로 변경된다.
4. 마지막 값 출력
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n -1][m -1]

# n, m을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))
    
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))