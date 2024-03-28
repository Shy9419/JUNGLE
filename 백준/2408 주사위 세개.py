a,b,c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    print(1000 + sorted([a, b, c])[1] * 100)
else:
    print(max(a, b, c) * 100)
    # if a > b and a > c:
    #     print(a * 100)
    # elif b > c and b > a:
    #     print(b * 100)
    # elif c > a and c > b:
    #     print(c * 100)
