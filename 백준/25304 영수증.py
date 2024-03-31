X = int(input())
N = int(input())

sum = 0

for i in range(N):
    a, b = map(int, input().split())
    sum += a*b      # 곱한 것을 sum 변수에 저장.
    
if sum == X:
    print('Yes')
else: 
    print('No')


