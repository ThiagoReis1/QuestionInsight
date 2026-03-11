from math import *

n = int(input("Entre com a quantidade de termos da serie: "))

soma = 0

sinal = -1

i = 0

while (i < n ):
	soma = soma + sinal * pow (i + 1, 3) / (8 + (2 * i + 1))											
	sinal = (-1) * sinal
	i = i + 1
print(round(soma,5))