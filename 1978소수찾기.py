n = int(input())    # n개의 수 를 입력
numbers = map(int, input().split())     # n개의 수를 띄어쓰기로 나눠서 정수형으로 입력 
sosu = 0    # 소수의 카운트를 위한 변수

for num in numbers:     # numbers를 num이란 변수에 넣으면서 소수를 찾는다.       # 소수가 아닌 값의 카운트를 위한 변수
    if num > 1:     # 만약 'num'에 1보다 큰 값이 오면 for문을 실행 (1을 소수에서 빼기 위해)
        no = 0
        for i in range(2, num):     # 2 부터 num-1 까지의 수를 i라는 변수에 할당
            if num % i == 0:    # 만약 num에 값이 i
                no += 1
        if no == 0:
            sosu += 1

# for num in numbers:     
#     if num == 1:
#         continue
    
#     for x in range(2,num):
#         if num % x == 0:
#             break
#     else:       # for문에 else문 if문에서 break를 했을 때 else블록이 실행됨.
#         sosu += 1
   
print(sosu)

# numbuers = [1, 3, 5]
# for i in numbuers:
#     if i ==3:
#         break
# else:
#     print()
