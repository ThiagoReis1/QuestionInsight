from math import *
x=eval(input("Angulo medido em radianos:"))
k=int(input("Quantidade de termos da serie:"))
s=0
while	(k>=0) and (x>=0):
	if	(k%2!=0):
		y=-(x**k)/(factorial(k*2))
		s=s+y
	if	(k%2==0):
		y=(x**k)/(factorial(k*2))
		s=s+y
	k=k-1
print(round(s, 6))