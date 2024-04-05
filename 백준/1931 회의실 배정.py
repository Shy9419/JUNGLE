import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N) :
    start, end = map(int, input().split())
    graph.append([end, start])
graph.sort()
cnt = 0
current = graph[0][1]
for end, start in graph :
    if current <= start :
        current = end
        cnt += 1
print(cnt)