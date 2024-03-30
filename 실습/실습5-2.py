# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
x, y = map(int, input().split())