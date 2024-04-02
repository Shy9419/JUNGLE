import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
k = int(input())

is_valied = True

def dfs(u):
    global is_valied
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False:
            team[v] = (team[u]+1)%2
            dfs(v)
        elif team[u] == team[v]:
            is_valied = False
            

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    team = [0] * (v + 1)    # 팀 나누기
    is_valied = True    # 각 테스트 케이스마다 is_valied 초기화
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, v + 1):
        if is_valied:
            dfs(i)
        else:
            break
    if is_valied:
        print("YES")
    else:
        print("NO")