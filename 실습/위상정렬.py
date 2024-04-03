import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

#진입차수
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    # result 에 출력할 결과를 담는다.
    result = []
    queue = deque()
    
    for i in range(1, n+1):
        # 진입차수가 0인 정점이라면 q에 추가한다.
        if indegree[i] == 0:
            queue.append(i)
        
    while queue:
        # 팝(디큐)가 되는 노드를 현재노드에 담는다.
        current = queue.popleft()
        # current 리스트에 값을 result 리스트에 추가한다.
        result.append(current)
        
        for i in graph[current]:
            # current로부터 나가는 간선 제거
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    # 출력 : 1 2 3 4 5
    for i in result:
        print(i, end=' ')
        
topology_sort()