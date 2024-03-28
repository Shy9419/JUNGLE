H,M = map(int, input().split())

if M < 45:
    H -= 1
    if H < 0:
        H = 23
    M += 15
elif M >= 45:
    H += 1
    if H > 23:
        H = 0
    M -= 15
print(H, M)



H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60
print(H, M-45)