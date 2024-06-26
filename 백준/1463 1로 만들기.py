import sys

input = sys.stdin.readline

n  = int(input())


d = [0] * 1000001

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)   # min(a1,a2) a1과 a2중에 작은 걸 반환한다.
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])
