n = int(input())

test = [int(input()) for _ in range(n)]

def dp(n):
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        for j in range(1, 4):
            d[i] += d[i-j]

    return d[n]


for i in test:
    print(dp(i))