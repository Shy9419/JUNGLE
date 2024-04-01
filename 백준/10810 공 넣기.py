n, m = map(int, input().split())

box = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())     # 정수로 입력을 받을 떄 i가 1부터 받기때문에 인덱스가 아닌 값으로 받으니까.
    for x in range(i,j+1):
        box[x-1] = k        # 값으로 받은 i를 인덱스 번호에 맞추기 위해 -1을 해줌

for i in range(len(box)):
    print(box[i], end=' ')
    

n   # 도현이가 가진 바구니 개수
m   # 도현이가 넣으려는 공의 수