x = int(input())
y = int(input())
if x > 0 and y > 0: print(1)
elif x < 0 and y > 0: print(2)
elif x < 0 and y < 0: print(3)
else:
    x > 0 and y > 0
    print(4)
    
x = int(input())
y = int(input())
print("3421"[x>0::2][y>0])