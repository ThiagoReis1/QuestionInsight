n=int(input())
i=0
s=0
x=0
while i<n:
	x=x+1
	s=s+(-1)**x*x**2/(6+2*x)
	i=i+1
print(round(s , 11))	