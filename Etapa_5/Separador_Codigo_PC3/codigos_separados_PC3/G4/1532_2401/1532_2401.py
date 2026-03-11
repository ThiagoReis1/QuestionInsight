from math import*
s=0
x=float(input())
k=int(input())
i=1
j=1
while(i<=k):
	s=s+((x)**j)/factorial(j)
	i=i+1
	j=j+2
print(round(s,9))