# [Do it! 실습 6-1] 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):    # 0부터n-1까지 i 값에 차례대로 반복
        for j in range(n-1, i, -1):     # n-1 부터 i까지 -1씩 j 값에 차례대로 반복
            if a[j-1] > a[j]:       # j-1이 j 보다 클 경우
                a[j-1], a[j] = a[j], a[j-1]     # 배열에서 순서를 바꿈 = 패스
                
if __name__ == '__main__':
    num = int(input())      # num이라는 변수에 정수형 입력값을 받음
    x = [None] * num    # 입력받은 num 만큼 x라는 배열을 늘림 ex) 5 x = [Noe, Noen, None, None, None]
    
    for i in range(num):        # i 라는 변수에 0부터 num-1만큼 대입
        x[i] = int(input(i))        # 대입한 i 변수를 x[] 리스트에 넣음.
        
    bubble_sort(x)      # 배열 x를 버블 정렬 시킨다.
    
    print()
    for i in range(num):    # i라는 변수에 num을 대입
        print(i,'=',x[i])   # print(인덱스 '=' 인덱스에 해당하는 값) 형식으로 출력 ex) num 이 3이고 리스트 x가 [10, 20, 30]인 경우 print(1, x[1]) -> 1 = 20