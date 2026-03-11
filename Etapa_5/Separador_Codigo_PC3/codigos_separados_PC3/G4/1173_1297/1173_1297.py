from math import*
n=int(input("valor de n"))
c=1
e=3
sj=-1**2/5+e
while c<n:
	sj=sj+c-1**2/5+e
	c=c+sj
print(round(n,10))
