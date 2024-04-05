n, k = map(int, input().split())
coin = []
count = 0

for _ in range(n):
    a = int(input())
    coin.append(a)
coin.reverse()
    
for i in coin:
    count += k//i
    k %= i
    
print(count)