def mergeLR(x,y):
    re = []
    i, j = 0,0
    
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            re.append(x)
            i += 1
        else:
            re.append(y)
            j += 1
            
    if j == len(y):
        while i < len(x):
            re.append(x[i])
            i += 1
    elif i == len(x):
        while j < len(y):
            re.append(y[j])
            i += 1
    return re

def mergesort(x):
    if len(x) <= 1:
        return(x)
    
    div = len(x)//2
    left = mergesort(x[:div])
    right = mergesort(x[div:])
    
    x = mergeLR(left,right)
    return x

if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input())
        
    mergesort(x)

    for i in range(num):
        print(x[i])
    
