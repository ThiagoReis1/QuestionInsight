# Hanna Soares Rodrigues - 21650885
# Avaliacao 04
# Exercicio 03

n = int(input("termos: "))

soma = 0
contador = 1
x = 1
y = 3
sinal = -1


while (contador <= n):
	soma = soma + ((x ** 2)/(5 + y))*sinal
	contador = contador + 1
	x = x + 1
	y = y + 2
	sinal = sinal * (-1)
	
print(round(soma, 10))
