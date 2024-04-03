n=int(input())  # 변수 'n'에 입력받은 숫자를 정수형으로 변환해서 넣어줌

for i in range(1,10):   # for문을 사용. 'i'라는 변수에 iterable 자료형 1-9까지를 range함수로 넣고
    print(n, '*', i, '=', n*i)      # 구구단의 형식으로 출력
    
n = int(input())
