import sys

num = int(input())

for i in range(1,num+1):
    A,B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A+B}')      # print(f'내용{숫자}') 형태