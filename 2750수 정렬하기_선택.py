from typing import MutableSequence


def selection_sort(a: MutableSequence):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
    
    
if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input())
        
    selection_sort(x)

    for i in range(num):
        print(x[i])


            
    