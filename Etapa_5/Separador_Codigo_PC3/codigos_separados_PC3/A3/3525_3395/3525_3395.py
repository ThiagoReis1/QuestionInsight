from math import*
x=float(input(""))
k=int(input(""))
i=1
soma=0
exp=1
while x<=k:
	k=k-1
	numerador=x**exp + x**(exp+2)
	denominador=factorial(k)
	termogeral=numerador/denominador
	soma=soma+1
	print(round(termogeral, 9))