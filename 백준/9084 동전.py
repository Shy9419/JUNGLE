import sys
t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    coin.insert(0,0)
    m = int(input())
    
    d = [0] * (m + 1)
    d[0] = 1
    
    for i in coin:
        for j in range(m+1):
            if i >= coin:
                d[i] += d[i - coin]
    print(d[m])