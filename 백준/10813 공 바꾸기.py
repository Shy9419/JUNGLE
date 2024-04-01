n, m = map(int, input().split())

box = [0] * n
temp = 0

for i in range(0,n):    
    box[i] = i+1
    
for _ in range(m):
    i, j = map(int, input().split())
    temp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = temp

for x in range(n):
    print(box[x], end=' ')