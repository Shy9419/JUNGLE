from typing import MutableSequence


def selection_sort(a: MutableSequence):
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[j]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j-=1
        a[j] = tmp

if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input())
        
    selection_sort(x)

    for i in range(num):
        print(x[i])


            
    