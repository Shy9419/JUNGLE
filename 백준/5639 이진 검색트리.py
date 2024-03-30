# import sys
# input = sys.stdin.readline

# arr = []
# while True:
#     try:
#         n = int(input())
#         arr.append(n)
#     except:
#         break
    
# def postorder(list):
#     if len(list) == 0:
#         return

#     left,right = [],[]      #arr에 for문을 돌려 값을 왼쪽 오른쪽으로 나누기 위해 빈 리스트 형성
#     root = arr[0]       # arr 배열에 0번 인덱스인 첫번째 값이 root이기 때문에 루트 노드로 설정
    
#     for i in range(1, len(list)):
#         if left[i] < root:
#             left.append[1:i]
#         else:
#             right.append[i:]
            
#     postorder(left)
#     postorder(right)
#     print(root)

# postorder(arr)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

def postorder(lst):
    if len(lst) == 0:
        return

    left, right = [], []
    root = lst[0]     
    
    for i in range(1, len(lst)):
        if lst[i] < root:
            left.append(lst[i])
        else:
            right.append(lst[i])

    postorder(left)     # 재귀를 돌려서 위에 함수 내용을 계속 반복한다. 루트를 만든다. 루트를 기준으로 왼쪽 오른쪽 자식을 어펜드한다. 
    postorder(right)
    print(root)

postorder(arr)
