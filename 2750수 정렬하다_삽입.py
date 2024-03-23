i=iter(open(0))
next(i)
print(*sorted(map(int,i)),sep='\n')