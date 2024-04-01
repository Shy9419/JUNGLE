A = [None] * 10

for i in range(1,10):
    A[i] = int(input())
    
max = A[1]
idx = 1

for i in range(2, len(A)):
    if A[i] > max:
        max = A[i]
        idx = i
print(max)
print(idx)