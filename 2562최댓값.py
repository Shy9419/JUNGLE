numbers = []    # 빈 리스트를 만든다. 9개의 정수가 담길 예정

# for _ in range(9):  # range함수를 사용해 횟수를 지정함.
#     i = int(input())    # i라는 변수에 입력받은 숫자를 정수로 변환해 넣는다.
#     numbers.append(i)   # 'numbers'라는 리스트에 정수로 변환된 i를 넣는다.

numbers = [int(input()) for _ in range(9)]
    
    
print(max(numbers))     #'numbvers' 리스트 max함수를 사용해 최댓값을 찾는다.
print(numbers.index(max(numbers))+1)    # index함수를 사용해 찾은 최댓값이 몇번째 인덱스에 있는지


