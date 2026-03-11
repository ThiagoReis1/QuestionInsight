from math import *
x=float(input())
k=int(input())

cont=0
i=0
cont2=1
while(cont<k):
	
	den=factorial(cont2*2-1)
	i=i+ (x**(cont*2+1))/den
	cont=cont+1
	cont2=cont2+1
print(round(i,9))