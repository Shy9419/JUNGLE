# A,B = map(int, input().split())
# print(A+B, A-B, A*B, A//B, A%B, sep='\n')
# # sep='\n'로 줄바꿈


myList = {1,2,3,4,5}
def add_one(n):
    return n+1

result2=list(map(add_one,myList))

print(result2)
