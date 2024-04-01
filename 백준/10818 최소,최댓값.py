n = int(input())
li = list(map(int, input().split()))

min = li[0]
max = li[0]

for i in range(len(li)):
    if li[i] < min:
        min = li[i]
    elif li[i] > max:
        max = li[i]
print(min, max)