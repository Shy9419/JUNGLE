# # 재귀알고리즘

# def recur(n):
#     if n > 0:
#         recur(n-1)
#         print(n)
#         recur(n-2)
        
# x = int(input)
# recur(x)

#각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8   # 각 열에서 퀸의 위치를 출력

def put():
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')    # pos의 i번째 요소를 출력하되, 출력 폭을 2로 지정하여 오른쪽으로 정려.
    print()
    
def set(i):
    """i열에 퀸을 배치"""
    for j in range(8):
        pos[i] = j      # 퀸을 j행에 배치
        if i ==7 :      # 모든 열에 퀸 배치를 종료
            put()
        else:
            set(i+1)        #다음 열에 퀸을 배치
            
set(0) # 0열에 퀸을 배치