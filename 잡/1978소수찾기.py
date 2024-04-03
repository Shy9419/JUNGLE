# n = int(input())    # n개의 수 를 입력
# numbers = map(int, input().split())     # n개의 수를 띄어쓰기로 나눠서 정수형으로 입력 
# sosu = 0    # 소수의 카운트를 위한 변수

# for num in numbers:     # numbers를 num이란 변수에 넣으면서 소수를 찾는다.       # 소수가 아닌 값의 카운트를 위한 변수
#     if num > 1:     # 만약 'num'에 1보다 큰 값이 오면 for문을 실행 (1을 소수에서 빼기 위해)
#         no = 0
#         for i in range(2, num):     # 2 부터 num-1 까지의 수를 i라는 변수에 할당
#             if num % i == 0:    # 만약 num에 값이 i
#                 no += 1
#         if no == 0:
#             sosu += 1

# # for num in numbers:     
# #     if num == 1:
# #         continue
    
# #     for x in range(2,num):
# #         if num % x == 0:
# #             break
# #     else:       # for문에 else문 if문에서 break를 했을 때 else블록이 실행됨.
# #         sosu += 1
   
# print(sosu)

# # numbuers = [1, 3, 5]
# # for i in numbuers:
# #     if i ==3:
# #         break
# # else:
# #     print()

# def __len__(self) -> int:
#     return self.ptr

n = int(input())
arr =list(map(int,input().split()))

def sieve(n):   # n까지 있는 모든 소수를 구하는 함수
    isprime = [True]*(n+1)  # isprime이라는 배열에 트루 값으로 채워진 n+1개의 배열(트루)를 만듦, n+1인 이유는 0부터 n까지 모든 인덱스를 만들기 위해서
    isprime[0] = isprime[1] = False # 0과 1은 소수가 아니기 때문에 모두 False로 바꿈
    sn = int(n**0.5)    # sn이라는 변수에 n을 루트 씌워준 값을 저장
    for i in range(2, sn+1):    # i를 2부터 sn까지 돌 수 있는 반복문 설정
        if isprime[i]:
            for j in range(i*i,n+1,i):  # i의 곱하기 2부터 n까지 i만큼 더하면서 자기자신을 제외하고
                isprime[j] = False  # isprime의 j값을 모두 False로 바꿈
    return isprime
    # return [x for x in range(n+1) if isprime[x]]  # 소수들을 리턴하는 리턴값(리스트컴플레이션)

isprime = sieve(1000)
result = 0
for x in arr:
    if isprime[x]:
        result += 1
print(result)