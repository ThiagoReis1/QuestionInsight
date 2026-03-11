valor = float(input())
codigo = input()

if codigo == 'C':
	cartao = int(input())
	if cartao == 1:
		total = valor
	else:
		total = valor + 7*valor/100
else:
	total = valor - valor*18/100

print(round(total, 2))