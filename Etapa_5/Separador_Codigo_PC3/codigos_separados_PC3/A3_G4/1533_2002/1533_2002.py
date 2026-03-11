from math import *

teta = float(input("Valor de x: "))
k = int(input("Número de termos da série: "))

soma = 1
i = 1

while i < k:
	soma = soma + teta**(2*i) / factorial(2*i)
	i = i + 1
	
serie = soma + 1
print(round(soma, 8))