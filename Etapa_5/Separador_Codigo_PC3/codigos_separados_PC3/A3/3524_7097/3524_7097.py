from math import*
x=float(input(""))
k=int(input(""))
v=0
acum=0
while x<=k:
	k=k-1
	numerador=x+(x^(k))+(x^(k))
	denominador=factorial(k-1)
	termogeral=numerador/denominador
print(round(termogeral,8))