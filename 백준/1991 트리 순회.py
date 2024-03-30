import sys

n = int(sys.stdin.readline().strip())
tree = {}       # {} 빈 딕셔너리를 생성하는 파이썬 문법

for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]      # tree라는 딕셔너리에 새로운 키와 값을 쌍을 추가합니다. ( 딕셔너리)
                                    # 새로운 키는 'root'이고, 해당 값은 리스트 '[left,right]'입니다.
                                    # 이 리스트는 'root' 노드의 왼쪽 자식과 오른쪽 자식의 값을 포함합니다.
def preorder(root):     # 전위 순회
    if root != '.':
        print(root, end='')   # root 출력
        preorder(tree[root][0])     # left
        preorder(tree[root][1])     # right
        
def inorder(root):      # 중위 순회
    if root != '.':
        inorder(tree[root][0])      # left
        print(root, end='')     # root
        inorder(tree[root][1])      # right
        
def postorder(root):        # 후위 순회
    if root != '.':
        postorder(tree[root][0])        # left
        postorder(tree[root][1])        # right
        print(root, end='')     # root
        
preorder('A')
print()
inorder('A')
print()
postorder('A')