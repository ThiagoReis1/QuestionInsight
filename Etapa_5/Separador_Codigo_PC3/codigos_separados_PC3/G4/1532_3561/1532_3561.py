from math import*
x=int(input("valor:"))
k=int(input("termos de serie:"))
i=0
e=0
while(i<k):
	e=  e+ (x**(2*i+1)/factorial(2*i+1))
	i=i+1
print(round(e,9))