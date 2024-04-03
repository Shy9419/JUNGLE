#하노이 탑 구현하기

def move(no, x, y):   # 'no'는 옮겨야 할 원반의 개수
    if no > 1:
        move(no -1 , x, 6 - x - y)      # '6 - x - y' = 중간기둥 
        
    print(x, y)
    
    if no > 1:
        move(no -1 , 6 - x - y, y)
        

        
n = int(input())
print(2**n-1)   # 2에 n승 -1 

if n <=20: move(n, 1, 3)

# #하노이 탑 구현하기

# def move(no, x, y):   # 'no'는 옮겨야 할 원반의 개수
#     """원반 no개를 x기둥에서 y기둥으로 옮김"""
#     if no > 1:
#         move(no -1 , x, 6 - x - y)      # '6 - x - y' = 중간기둥 
        
    
    
#     if no > 1:
#         move(no -1 , 6 - x - y, y)
        
#     print(f'원반 [{no}번을(를) {x}기둥에서 {y}기둥으로 옮깁니다.]')
        
# n = int(input())

# move(n, 1, 3)