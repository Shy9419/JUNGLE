# def floyd(W):
#     D = W
#     n = len(W)
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 D[i][j] = min(D[i][j], D[i][k] + D[k][j])
#     return D

# INF = 999
# W = [
#     [0,1,INF,1,5],
#     [9,0,3,2,INF],
#     [INF,INF,0,4,INF],
#     [INF,INF,2,0,3],
#     [3,INF,INF,INF,0]
# ]

# D = floyd(W)
# for i in range(len(D)):
#     print(D[i])
    
def floyd2(W):
    n = len(W)
    D = W
    P = [[-1] * n for _ in range(n)]        # -1로 행렬을 채워놓고 만약에 D[i][j] + D[k][j] 가 크면
    for k in range(n):                      # 그 값을 P[i][j]에 넣어놓자.
        for i in range(n):
            for j in range(n):
                if (D[i][j] > D[i][k] + D[k][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
    return D, P

def path(P,u,v):
    if P[u][v] != -1:
        path(P,u,P[u][v])
        print('v%d'%(P[u][v]), end='->')
        path(P,P[u][v], v)
        
INF = 999
W = [
    [0,1,INF,1,5],
    [9,0,3,2,INF],
    [INF,INF,0,4,INF],
    [INF,INF,2,0,3],
    [3,INF,INF,INF,0]
]

D, P = floyd2(W)
for i in range(len(D)):
    print(D[i])
for i in range(len(P)):
    print(P[i])
    
u = 4
v = 2
print('shortest path from v%d to v%d: '%(u, v), end='')
print('V%d'%(u), end='->')
path(P,u,v)
print('V%d'%(v), end=' ')


# import sys

# INF = sys.maxsize

# def Floyd_Warshall():
#     dist = [[INF] * n for i in range(n)]    # 최단 경로를 담는 배열
    
#     for i in range(n):  # 최단 경로를 담는 배열 초기화
#         for j in range(n):
#             dist[i][j] = a[i][j]
            
#     for k in range(n):
#         for i in range(n):
#             for i in range(n):
#                 if dist[i][j] > dist[i][k] + dist[k][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
#     return dist

# n = 4 # 정점의 수
# a = [[0,2,INF,4], [2,0,INF,5], [3, INF, 0, INF], [INF, 2, 1, 0]]

# dist = Floyd_Warshall()

# for i in range(n):
#     for j in range(n):
#         print(dist[i][j], end='')
#     print()
    