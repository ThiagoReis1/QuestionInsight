from math import *
x = float(input("Um numero real: "))
k = int(input("Quantidade de termos da serie: "))
i = 1
soma = 1
while i <= k:
	soma = soma + ((x**i)/factorial(i))
	i = i + 1
print(round(soma, 9))