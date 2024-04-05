arr = []
for i in range(10):
    a = int(input())%42
    if a not in arr:
        arr.append(a)

print(len(arr))