from math import*
x=float(input())
k=int(input())
tot=0
lol=0
n=0
while(lol<k):
	tot=tot+((x**n)/factorial(n))
	n=n+1
	lol=lol+1
print(round(tot,9))