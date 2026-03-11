# Hanna Soares Rodrigues - 21650885
# Avaliacao 04
# Exercicio 02

from math import*
n = int(input("Digite o numero de termos: "))

contador = 1
acumulador1 = 1
acumulador2 = 1
sinal = -1
soma = 0

while (contador <= n):
	soma = soma + (sqrt(acumulador1)/ (9 + acumulador2))*sinal
	acumulador1 = acumulador1 + 1
	acumulador2 = acumulador2 + 2
	contador = contador + 1
	sinal = sinal * (-1)
print(round(soma, 6))
