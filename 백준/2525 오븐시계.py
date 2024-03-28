H, M = map(int, input().split())
cook = int(input())

H += cook // 60
M += cook % 60
if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H, M)