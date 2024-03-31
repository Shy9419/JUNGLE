import sys

num = int(input())

for i in range(1, num+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')