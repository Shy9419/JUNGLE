n, s = map(int, input().split())
li = [None] * n

for i in range(n):
    li[i] = input()
    
count = 0
for i in range(n-1):
    for j in range(0, n-1 1):
        if li[i] + li[j] = s:
            count += 1

print(count)
