X = int(input())
Y = int(input())

numero = X
soma = 0

while numero <= Y:
	if numero % 2 == 0:
		soma = soma + numero
	numero = numero + 1

print(soma)