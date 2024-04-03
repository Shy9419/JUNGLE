# 시작점에 연결된 vertex 찾기
# 연결된 vertex를 계속해서 찾음(끝날 때 까지)
# 더이상 연결된 vertex 없을 경우 다음.

"""
1. 아이디어
-2중 for, 값 1 && 방문 X = > DFS
-DFS를 통해 찾은 값을 저장 후 정렬
2. 시간복잡도
-DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 >> 가능

3. 자료구조
-그래프 저장 : intp[][]

"""

import sys
input = sys.stdin.readline
N = int(input())
map_data = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in  range(N)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)
        

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)
            
            # 방문 체크 표시
            # DFS 로 크기 구하기
            # 크기를 결과 리스트에 넣기
            # Bsf : 함수 호출, 리턴값으로 크기
result.sort()
print(len(result))
for i in result:
    print(i)
            
