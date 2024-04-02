import sys
input = sys.stdin.readline
k = int(input())

is_valied = True

def dfs(u):
    global is_valied
    visited[u] = True
    for v in graph[u]:
        if visited == False:
            team[v] = (team[u]+1)%2
            dfs(u)
        elif team[u] == team[v]:
            is_valied = False
            

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    team = [0] * (v + 1)    # 팀 나누기
    
    for _ in range(v + 1):
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