n = int(input())
li = list(map(int, input().split()))
v = int(input())

count = 0

for i in range(len(li)):
    if li[i] == v:
        count += 1

print(count)