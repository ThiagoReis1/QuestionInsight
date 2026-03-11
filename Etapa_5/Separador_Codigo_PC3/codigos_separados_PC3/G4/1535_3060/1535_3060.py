from math import *
x = float(input("Valor de X: "))
k = int(input("No. de termos: "))
i = 0
soma = 0

while (i < k):
	soma = soma + ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
	i = i + 1
print(round(soma, 6))
#é alguma coisa na fórmula, tenta ajeitar depois, passa pra 2