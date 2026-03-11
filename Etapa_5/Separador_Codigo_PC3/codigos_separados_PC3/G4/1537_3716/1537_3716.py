from math import*
x=float(input("numero real:"))
k=int(input("numero de termos:"))

t=1
e=0

while t<=k:
	e=e+(x**(t-1)/factorial(t-1))
	t=t+1
	
print(round(e,9))
	