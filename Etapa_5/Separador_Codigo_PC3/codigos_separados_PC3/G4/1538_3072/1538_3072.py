from math import *
x = float(input("Valor de x: "))
k = int(input("Numero de  termos: "))
i = 0
soma = 1

while(i < k):
	soma = soma + ((-1) ** i) * (x ** (2 * i))
	i = i + 1
r = (1* (x ** 2)) * soma	
print(round(r,8))
