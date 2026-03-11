from math import*
x=float(input("x: "))
k=int(input("k: "))
l=0
n=1
while(l<k):
	l=l-(x**n/n)*(-1)**(n+1) 
	n=n+1
print(round(l,10))
