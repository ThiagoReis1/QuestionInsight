from math import*
x=float(input("De o numero real x: "))
k=int(input("De o indice da soma parcial: "))

senhx=0
i=0
while(i<k):
	senhx=senhx+x**(2*i+1)/factorial(2*i+1)
	i=i+1
print(round(senhx,9))