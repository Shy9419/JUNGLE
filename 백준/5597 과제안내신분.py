a = [i for i in range(1,31)]
    
for _ in range(28):
    b = int(input())
    a.remove(b)
        
print(min(a))
print(max(a))
    



    
# for i in range(28):
#     b = int(input())
#     a.pop(b)
    
# print(a)