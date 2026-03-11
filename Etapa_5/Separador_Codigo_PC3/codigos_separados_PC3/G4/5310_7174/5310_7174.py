from math import *
x=float(input("numero:  "))
k=int(input("termos:  "))
cont=0
d=1
s=0
if(k>0):
	while(cont<k):
		s=s+x/factorial(d)
		d=d+2
		cont=cont+1

print(round(s, 8))