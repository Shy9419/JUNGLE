n, m = map(int, input().split())
list = []

for i in range(1, n+1):
    list.append(i)


for x in range(m):
    i, j = map(int, input().split())
    temp = list[i-1:j]
    temp.reverse()
    list[i-1:j] = temp
    
for x in range(n):
    print(list[x], end=' ')
    