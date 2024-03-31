while True:
    try:    # 발생할 예외 지정
        A, B = map(int, input().split())
        print(A+B)
    except: # 지정한 예외가 발생 했을 때 예외를 처리할 내용
        break
    
    