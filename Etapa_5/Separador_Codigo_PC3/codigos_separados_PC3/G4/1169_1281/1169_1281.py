from math import *
n=int(input("valor"))
s=0
k=n-1
while (n>=1):
	if n%2==0:
		l=1	
		x=sqrt(n)/(9+(n+k))*l
		n=n-1
		k=k-1
		l=l*(-1)
	else:
		l=-1	
		x=sqrt(n)/(9+(n+k))*l
		n=n-1
		k=k-1
		l=l*(-1)
	s=s+x
print(round(s, 6))	
		