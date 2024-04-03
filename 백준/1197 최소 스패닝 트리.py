# #간선의 개수가 n-1인 연결 트리가 될 때까지 간선을 하나씩 제거
# import sys, heapq

# V, E = map(int, sys.stdin.readline().strip().split())       # 첫 번째 줄에서 정점의 수 V 와 간선의 수 E 를 입력 받는다.

# arr = [[] for _ in range(V)]                                # 각 정점의 인접 리스트를 저장할 리스트 arr을 초기화 합니다.
# for _ in range(E):                                          # 입력된 간선의 수 만큼 반복합니다.
#     v1, v2, d = map(int, sys.stdin.readline().strip().split())      # 간선의 정보를 입력 받습니다. 여기서 'v1'과 'v2'는
#                                                                     # 간선이 연결하는 두 정점이고, 'd'는 간선의 가중치입니다.
#     arr[v1-1].append([v2-1, d])                                     # 'V1'과 'v2'를 연결하는 간선의 정보를 'v1'의 인접 리스트
#                                                                     # 에 추가합니다. 이때 가중치 'd'와 연결된 정점 'v2'를 함꼐
#                                                                     # 저장합니다.
#     arr[v2-1].append([v1-1, d])

# ### Prim
# que, dist, cnt = [], 0, 0
# vi = [False for _ in range(V)]
# heapq.heappush(que, (0, 0)) # dist, start vertex

# while cnt < V:
#     (d, v2) = heapq.heappop(que)
#     if not vi[v2]:
#         vi[v2] = True
#         dist += d
#         cnt += 1

#         for e in arr[v2]:
#             if not vi[e[0]]:
#                 heapq.heappush(que, [e[1], e[0]])

# print(dist)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
edges = []
set_list = [0] * (V + 1)
result = 0

for _ in range (E) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

# 리스트에 부모 값들 초기화
for i in range (1, V + 1):     #노드번호
    set_list[i] = i     # '0'으로 채워진 set_list함수에 1부터 입력받을 Vertex의 수만큼 숫자로 채움
    
def find (parent, x) :      # 배열 set_list를 parent로 가져옴. x = a 노드번호
    if parent[x] != x :     # 만약 a노드에 부모값이 노드번호와 같지 않다면
        parent[x] = find(parent, parent[x])     # set_list에서 같지 않은 값을 노드번호로 하는 
    return parent[x]

def union (parent, x, y):
    x = find (parent, x)
    y = find (parent, y)
    if x > y :
        parent[x] = y
    else :
        parent[y] = x
        
for u in graph:
    cost, a, b = u
    if find (set_list, a) != find (set_list, b) :
        union (set_list, a, b)
        result += cost
print (result)
