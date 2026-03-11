from math import*
x = float(input("valor x:"))
k = int(input("valor de k:"))
cont = 1
soma = 1
a = 2
while(cont < k):
	soma = soma + (x**(a)/factorial(a))
	a = a + 2
	cont = cont + 1
print(round(soma, 8))