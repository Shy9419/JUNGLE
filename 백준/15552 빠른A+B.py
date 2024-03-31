import sys

num = int(input())

for i in range(num):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)
